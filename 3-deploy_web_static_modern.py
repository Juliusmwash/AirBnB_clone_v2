#!/usr/bin/python3
import sys
import os
from fabric import Connection
from os.path import isdir, isfile
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static
    folder of AirBnB Clone repo
    """
    conn = Connection("localhost")
    if isdir("versions") is False:
        try:
            conn.local('mkdir versions')
        except:
            return None
    now = datetime.now()
    timestamp = now.strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_{}.tgz'.format(timestamp)
    try:
        conn.local('tar -czvf {} web_static'.format(archive_path))
        return archive_path
    except:
        return None

f1 = f2 = f3 = do_pack()
archive_path = f1
file = f2.split('/')[1]
file_no_ext = f3.split('/')[1].split('.')[0]
extract_path = '/data/web_static/releases/' + file_no_ext + '/'


def do_deploy(archive_path, conn):
    """
    Distributes an archive to your web servers, using
    the function do_deploy
    """
    if not isfile(archive_path):
        return False

    conn.run('mkdir -p tmp')
    conn.put(archive_path, 'tmp')
    conn.run(f'mkdir -p {extract_path}')
    conn.run(f'sudo tar -xzf tmp/{file} -C {extract_path}')
    conn.run(f'rm -rf tmp/{file}')
    conn.run(f'sudo chmod -R +rw {extract_path}/web_static')
    conn.run(f'sudo mv {extract_path}/web_static/* {extract_path}')
    conn.run(f'rm -rf {extract_path}/web_static')
    conn.run('rm -rf /data/web_static/current')
    conn.run(f'ln -s {extract_path} /data/web_static/current')


def deploy():
    """ Calls all the functions to auto complete tasks"""
    hosts = ['100.25.16.12', '35.153.17.49']
    for host in hosts:
        conn = Connection(host, user='ubuntu', connect_kwargs={'key_filename': '/home/julius/.ssh/school'})
        do_deploy(archive_path, conn)


deploy()
