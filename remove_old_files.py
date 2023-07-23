#!/usr/bin/python3
from fabric import Connection


def do_clean(number=0):
    """
    Deletes out-of-date archives.
    """
    connections = []
    connections.append(Connection('localhost'))
    for conn in connections:
        result = conn.local('ls -tr versions', hide=True)
        str_result = str(result.stdout)
        print(f"result: {str_result}")
        archives = result.stdout.strip().split('\n')
        str_archives = str(archives)
        print(f"archives: {str_archives}")
        num_archives_to_delete = max(0, len(archives) - number)
        if number == 0 or number == 1:
            archives_to_delete = archives[:-1]
            for archive in archives_to_delete:
                result = conn.local(f'rm versions/{archive}')
        else:
            if num_archives_to_delete > 0:
                archives_to_delete = archives[:num_archives_to_delete]
                for archive in archives_to_delete:
                    result = conn.local(f'rm versions/{archive}')

do_clean(2)
