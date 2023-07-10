#!/usr/bin/python3
""" Defines do_clean function """
from fabric import Connection


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
    for conn in connections:
        result = conn.run('ls -tr versions', hide=True)
        archives = result.stdout.strip().split('\n')
        num_archives_to_delete = max(0, len(archives) - number)
        if num_archives_to_delete > 0:
            archives_to_delete = archives[:num_archives_to_delete]
            for archive in archives_to_delete:
                conn.run(f'rm versions/{archive}')

        print(f' Deleted {num_archives_to_delete} archives in the versions folder')

        # Delete unnecessary archives in the /data/web_static/releases folder on both web servers
        with c.cd('/data/web_static/releases'):
            result = c.run('ls -tr', hide=True)
            releases = result.stdout.strip().split('\n')

            releases_to_delete = releases[:num_archives_to_delete]
            for release in releases_to_delete:
                c.run(f'rm -rf {release}')

        print(f'Deleted {num_archives_to_delete} releases in the /data/web_static/releases folder')

    else:
        print('No archives to delete')


# Define your hosts
hosts = ['<IP web-01>', '<IP web-02>']

# Create a task with the hosts
clean_archives = task(hosts=hosts)(do_clean)

