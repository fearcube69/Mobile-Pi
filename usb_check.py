import subprocess

def detect_file_system(device_path):
    try:
        result = subprocess.run(['blkid', '-s', 'TYPE', '-o', 'value', device_path], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip().upper()
        else:
            return 'Unknown'
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    device_path = "/media/roxy"  # Replace with the actual device path of your USB drive
    file_system = detect_file_system(device_path)

    if file_system:
        print(f"The USB drive is using the {file_system} file system.")
    else:
        print("Unable to detect the file system.")

if __name__ == "__main__":
    main()
