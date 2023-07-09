#!/usr/bin/python3
from fabric import Connection
from os.path import isdir
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static
    folder of AirBnB Clone repo
    """
    conn = Connection("localhost")
    print("conn made")
    if isdir("versions") is False:
        try:
            print("making dir")
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


do_pack()
