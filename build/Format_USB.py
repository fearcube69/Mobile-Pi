import os
import subprocess

def list_directories(base_path):
    # List all directories under the specified base path
    return [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

def get_mounted_devices(target_mount_point):
    try:
        # Read the contents of /proc/self/mounts
        with open('/proc/self/mounts', 'r') as mounts_file:
            for line in mounts_file:
                fields = line.split()
                if len(fields) >= 2 and fields[1] == target_mount_point:
                    # Print device, mount point, and file system type
                    print(f"Device: {fields[0]}, Mount Point: {fields[1]}, File System Type: {fields[2]}")
    except FileNotFoundError:
        print("/proc/self/mounts not found. Are you running on a Linux system?")

def main():
    # Specify the base path
    base_path = '/media/roxy'

    # List all directories under /media/roxy
    directory_names = list_directories(base_path)

    # Print the names of the directories
    for name in directory_names:
        print(name)

    # Get the last directory name (if any)
    if directory_names:
        target_mount_point = os.path.join(base_path, directory_names[-1])
        print(f"\nTarget Mount Point: {target_mount_point}\n")

        # Call the get_mounted_devices function
        get_mounted_devices(target_mount_point)

        # Define the device identifier of the USB flash drive
        device_identifier = subprocess.check_output(['df', target_mount_point]).decode().split('\n')[-2].split()[0]

        # Unmount the USB flash drive
        subprocess.run(['sudo', 'umount', device_identifier])

        # Format the USB flash drive with the FAT32 file system
        subprocess.run(['sudo', 'mkfs.vfat', device_identifier])

        # Check the exit status of the mkfs command
        if subprocess.run(['sudo', 'mkfs.vfat', device_identifier]).returncode == 0:
            print("Formatting successful.")
        else:
            print("Formatting failed.")

if __name__ == "__main__":
    main()
