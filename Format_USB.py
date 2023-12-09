# import os
# import subprocess
#
# def get_usb_devices():
#   devices = os.listdir('/media/roxy')
#   usb_devices = [device for device in devices if device.startswith('sd')]
#   return usb_devices
#
# def get_file_system(device):
#   output = subprocess.check_output(['blkid', device]).decode('utf-8')
#   file_system = output.split('TYPE=')[1].split()[0]
#   return file_system
#
# def format_usb(device, file_system):
#   subprocess.run(['mkfs', '-t', file_system, device])
#
# usb_devices = get_usb_devices()
# for device in usb_devices:
#   file_system = get_file_system(device)
#   print(f'The file system of {device} is {file_system}.')
#   format_usb(device, file_system)
#   print(f'{device} has been formatted to {file_system}.')

import subprocess

def get_mounted_devices():
    try:
        result = subprocess.run(['./wipe.sh'], capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error: {result.stderr.strip()}"
    except Exception as e:
        return f"Error: {e}"

def main():
    output = get_mounted_devices()
    print(output)

if __name__ == "__main__":
    main()
