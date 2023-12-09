#!/bin/bash

device_name=$(df /media/roxy | grep -v Filesystem | awk '{print $1}')


target_mount_point="$device_name"

get_mounted_devices() {
    awk -v target="$target_mount_point" '$2 == target {print "Device: " $1 ", Mount Point: " $2 ", File System Type: " $3}' /proc/self/mounts
}

main() {
    get_mounted_devices
}

main

