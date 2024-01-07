#!/bin/bash

# Function to wipe the mounted drive
function wipe_drive() {
 echo "Unmounting the drive..."
 fuser -k /media/$USERNAME
 sleep 1
 echo "Wiping the drive..."
 mkfs.$FORMAT $MOUNTED_DEVICE
 echo "Remounting the drive..."
 mount $MOUNTED_DEVICE /media/$USERNAME
 echo "The drive has been wiped."
}

# Get the username from the whoami command
USERNAME=$(whoami)
WIPE="false" # Set to true to wipe the drive

if mountpoint -q "/media/$USERNAME"; then
 MOUNTED_DEVICE=$(df -h /media/$USERNAME --output=source | tail -n1)
 FORMAT=$(lsblk -no FSTYPE $MOUNTED_DEVICE)
 echo "/media/$USERNAME is a mount point with format: $FORMAT"
 if [ "$WIPE" = "true" ]; then
     wipe_drive
 fi
else
 echo "/media/$USERNAME is not a mount point"
fi