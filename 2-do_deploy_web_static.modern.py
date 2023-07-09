#!/usr/bin/python3
"""
Defines do_deploy function
"""

import sys
import os
from fabric import Connection
from os.path import isdir, isfile, join

hosts = ['100.25.16.12', '35.153.17.49']
connections = []
for host in hosts:
    conn = Connection(host, user='ubuntu', connect_kwargs={'key_filename': '/home/julius/.ssh/school'})
    connections.append(conn)

def get_file():
    """
    get name of the compressed web_static file
    """
    files = os.listdir('versions')
    for file in files:
        file_name = os.path.join('versions', file)
        if isfile(file_name):
            """file_name = os.path.splitext(file)[0]"""
            return file_name


archive_path = get_file()
file = get_file().split('/')[1]
file_no_ext = get_file().split('/')[1].split('.')[0]
extract_path = '/data/web_static/releases/' + file_no_ext + '/'


def do_deploy(archive_path, conn):
    """
    Distributes an archive to your web servers, using
    the function do_deploy
    """
    if not isfile(archive_path):
        return False
    conn.run('mkdir tmp')
    conn.put(archive_path, 'tmp')
    conn.run(f'mkdir -p {extract_path}')
    conn.run(f'sudo tar -xzf tmp/{file} -C {extract_path}')
    conn.run(f'rm -rf tmp/{file}')
    conn.run(f'sudo chmod -R +rw {extract_path}/web_static')
    conn.run(f'sudo mv {extract_path}/web_static/* {extract_path}')
    conn.run(f'rm -rf {extract_path}/web_static')
    conn.run('rm -rf /data/web_static/current')
    conn.run(f'ln -s {extract_path} /data/web_static/current')


for connctn in connections:
    do_deploy(archive_path, connctn)
