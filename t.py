#!/usr/bin/python3
from datetime import datetime
now = datetime.now()
timestamp = now.strftime('%Y%m%d%H%M%S')
archive_path = 'versions/web_static_{}.tgz'.format(timestamp)
print(archive_path)
