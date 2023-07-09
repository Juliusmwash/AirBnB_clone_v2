#!/usr/bin/python3
"""
Defines do_deploy function
"""

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


def do_deploy(archive_path, conn):
    """
    Distributes an archive to your web servers, using
    the function do_deploy
    """
    if not isfile(archive_path):
        return False
    file = archive_path.split('/')[1]
    conn.run('sudo mkdir -p /home/ubuntu/tmp_test')
    conn.run('sudo chown ubuntu:ubuntu /home/ubuntu/tmp_test')
    conn.put(file, '/home/ubuntu/tmp_test')
    conn.run('ls tmp_test')


for connctn in connections:
    do_deploy(archive_path, connctn)
