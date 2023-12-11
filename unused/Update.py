#!/usr/bin/env python3

import os
import subprocess
import getpass

def get_current_user():
    return os.getlogin()

def list_directory_names():
    current_user = get_current_user()
    directory_names = []

    # List all directories under /media/current_user
    for dir in os.listdir(f'/media/{current_user}/'):
        directory_names.append(dir)

    return directory_names

def print_directory_names(directory_names):
    for name in directory_names:
        print(name)

def get_target_mount_point(directory_names):
    if not directory_names:
        return None
    return f'/media/{get_current_user()}/{directory_names[0]}'

def get_mounted_devices(target_mount_point):
    with open('/proc/self/mounts', 'r') as mounts_file:
        for line in mounts_file:
            fields = line.split()
            if len(fields) >= 2 and fields[1] == target_mount_point:
                return f"Device: {fields[0]}, Mount Point: {fields[1]}, File System Type: {fields[2]}"

def run_command_with_sudo(command):
    password = getpass.getpass("Enter your password: ")
    sudo_command = f"echo {password} | sudo -S {command}"
    result = subprocess.run(sudo_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode == 0:
        print("Command executed successfully.")
        print(result.stdout)
    else:
        print("Error executing command.")
        print(result.stderr)

def main():
    directory_names = list_directory_names()
    print_directory_names(directory_names)

    target_mount_point = get_target_mount_point(directory_names)
    if target_mount_point:
        print(target_mount_point)

        mounted_devices_info = get_mounted_devices(target_mount_point)
        print(mounted_devices_info)

        device_identifier = os.popen(f"df {target_mount_point} | tail -n1 | awk '{{print $1}}'").read().strip()

        # Unmount the USB flash drive
        run_command_with_sudo(f"umount {device_identifier}")

        # Format the USB flash drive with the FAT32 file system
        run_command_with_sudo(f"mkfs.vfat {device_identifier}")

    else:
        print("No target mount point found.")

if __name__ == "__main__":
    main()
