import os
from psutil import disk_partitions

def which_filesystem(directory_or_file):
    # get all mounted partitions:
    partitions = disk_partitions(all=True) # including mount points
    partitions.sort(key = lambda x: len(x.mountpoint), reverse = True) # longest mountpoint first: /home/blabla is more specific than /
    fstype = None # default
    # find which mountpoint is first (and thus longest) match:
    if os.path.isfile(directory_or_file) or os.path.isdir(directory_or_file):
        for partition in partitions:
            if directory_or_file.startswith(partition.mountpoint):
                fstype = partition.fstype
                # found and done
                break
    return fstype

