#!/usr/bin/python3
""" Defines do_clean function """
from fabric import Connection
import sys


def make_connections():
    """Create connections to the web servers"""
    connections = []
    hosts = ['100.25.16.12', '35.153.17.49']
    for host in hosts:
        conn = Connection(host, user='ubuntu', connect_kwargs={
            'key_filename': '/home/julius/.ssh/school'})
        connections.append(conn)
    return connections


def do_clean(number=0):
    """
    Deletes out-of-date archives.
    """

    connections = make_connections()

    conn = Connection('localhost')
    result = conn.local('ls -tr versions', hide=True)
    archives = result.stdout.strip().split('\n')
    num_archives_to_delete = max(0, len(archives) - number)
    if number == 0 or number == 1:
        archives_to_delete = archives[:-1]
        for archive in archives_to_delete:
            print(f'archive: {archive}')
            conn.local(f'rm versions/{archive}')
    else:
        if num_archives_to_delete > 1:
            archives_to_delete = archives[:num_archives_to_delete]
            for archive in archives_to_delete:
                conn.local(f'rm versions/{archive}')

    for conn in connections:
        with conn.cd('/data/web_static/releases'):
            result = conn.run('ls -tr', hide=True)
            directories = result.stdout.strip().split('\n')
            num_directories_to_delete = max(0, len(directories) - number)
            if number == 0 or number == 1:
                directories_to_delete = directories[:-1]
                for directory in directories_to_delete:
                    conn.run(f'sudo rm -rf {directory}')
            else:
                if num_directories_to_delete > 1:
                    directories_to_delete = \
                            directories[:num_directories_to_delete]
                    for directory in directories_to_delete:
                        conn.run(f'sudo rm -rf {directory}')


if len(sys.argv) > 1:
    number = int(sys.argv[1])
else:
    number = 0
do_clean(number)
