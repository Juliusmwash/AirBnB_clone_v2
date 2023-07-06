#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static
    folder of AirBnB Clone repo
    """
    local('mkdir -p versions')

    now = datetime.now()
    timestamp = now.strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_{}.tgz'.format(timestamp)

    result = local('tar -czvf {} web_static'.format(archive_path))

    if result.succeeded:
        return archive_path
    else:
        return None
