#!/usr/bin/env python3
# coding: utf-8



# mount type
# df -h <dir>
# mount | grep /dev/vdb | awk '{ print $5 }'  | sort -u

'''
$ df -h .
Filesystem      Size  Used Avail Use% Mounted on
/dev/vdb         10G  6.0G  3.8G  62% /

$ mount | grep /dev/vdb | awk '{ print $5 }'  | sort -u
btrfs


'''
import os


def mount_type_of_directory_old(directory):
    # returns mount type of directory (or file), with external commands df and mount
    try:
        cmd = f"df {directory}"
        df_output = os.popen(cmd).readlines()
        device = df_output[1].split()[0]  # for example '/dev/nvme0n1p2' ... or an exception
    except:
        # no valid result
        return None

    cmd = f"mount"
    mount_output = os.popen(cmd).readlines()
    # get first matching line
    for line in mount_output:
        if line.startswith(device):
            return (line.split(" ")[4])
            # done
    return None


def mount_type_of_directory(directory):
    directory = os.path.expanduser(directory)
    if not os.path.exists(directory):
        return None

    # map all mount info from /etc/mtab into a dictionary
    filesystem = {}
    with open('/etc/mtab') as f:
        mountlist = f.readlines()
        for line in mountlist:
            mountpoint, filesystemtype = line.split(" ")[1:3]  # second and third elements from /etc/mtab
            filesystem[mountpoint] = filesystemtype

    pathlist = directory.split(os.sep)  # ['', 'home', 'sander', 'git', 'sabnzbd', 'sabnzbd', 'utils']
    # start with full path, and make shorter, until match in filesystem[]
    length = len(pathlist)
    while length > 1:
        semipath = os.sep.join(pathlist[:length])
        try:
            filesystemfound = filesystem[semipath]
            return (filesystemfound)
        except:
            # no match yet, no problem
            pass
        # make path shorter
        length = length - 1

    if length <= 1:
        filesystemfound = filesystem["/"]
        return (filesystemfound)




print(mount_type_of_directory_old(r"/home/sander/git/sabnzbd/sabnzbd/utils"))
print(mount_type_of_directory(r"/home/sander/git/sabnzbd/sabnzbd/utils"))


print(mount_type_of_directory_old("~"))
print(mount_type_of_directory("~"))




