#!/bin/bash

current_user=$(whoami)
# Initialize an empty array to store the directory names
directory_names=()

# List all directories under /media/roxy
for dir in /media/"$current_user"/*/; do
   # Get the name of the directory
   directory_name=$(basename "$dir")

   # Add the name of the directory to the array
   directory_names+=("$directory_name")
done

# Print the names of the directories
for name in "${directory_names[@]}"; do
   echo "$name"
done

# Select the last directory name
target_mount_point="/media/$current_user/${directory_names[-1]}"

echo "$target_mount_point"

get_mounted_devices() {
    awk -v target="$target_mount_point" '$2 == target {print "Device: " $1 ", Mount Point: " $2 ", File System Type: " $3}' /proc/self/mounts
}

main() {
    get_mounted_devices
}

main

# Define the device identifier of the USB flash drive
device_identifier=$(df "$target_mount_point" | tail -n1 | awk '{print $1}')

# Unmount the USB flash drive with sudo using password from pass.txt
{ echo "$(cat pass.txt)"; echo "echo '';"; } | sudo -S umount "$device_identifier"

# Format the USB flash drive with the FAT32 file system with sudo using password from pass.txt
{ echo "$(cat pass.txt)"; echo "echo '';"; } | sudo -S mkfs.vfat "$device_identifier"

# Check the exit status of the mkfs command
if [ $? -eq 0 ]; then
    echo "Formatting successful."
else
    echo "Formatting failed."
fi
