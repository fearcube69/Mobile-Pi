#!/bin/bash

# Script to manage Python virtual environment, install a package, and configure swap
# shellcheck disable=SC2034
name_user=$(whoami)

# Set the path to the virtual environment
VENV_PATH="$(dirname "$(readlink -f "$0")")/venv"

sudo apt-get install python3

# Check if the virtual environment exists
if [ -d "$VENV_PATH" ]; then
    # Virtual environment exists, activate it
    echo "Activating existing virtual environment..."
    source "$VENV_PATH/bin/activate"
else
    # Virtual environment does not exist, create and activate it
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_PATH"
    source "$VENV_PATH/bin/activate"
fi

# Install dependencies from requirements.txt
if pip install -r requirements.txt; then
    echo "Dependencies installed successfully"
else
    echo "Error installing dependencies" | tee -a installation_errors.txt
fi

# Configure swap
if {
  sudo dphys-swapfile swapoff &&
  echo "CONF_SWAPSIZE=2000" | sudo tee /etc/dphys-swapfile &&
  sudo dphys-swapfile setup &&
  sudo dphys-swapfile swapon
} || {
  echo "Swap configuration failed" | tee -a installation_errors.txt
}; then
  echo "Swap configured successfully"
else
  echo "Error configuring swap" | tee -a installation_errors.txt
fi

# Modify sudoers file
echo "$name_user ALL=(ALL:ALL)" | sudo tee -a /etc/sudoers

# Display activation instructions
echo "Virtual environment activated."
echo "To deactivate the virtual environment, run: deactivate"

# Install ClamAV and configure
sudo apt update
sudo apt install clamav clamav-daemon -y
sudo systemctl enable clamav-daemon
sudo freshclam
sudo /etc/init.d/clamav-freshclam stop
sudo freshclam
sudo /etc/init.d/clamav-freshclam start
echo -e "[Service]\nExecStartPre=/bin/mkdir -p /run/clamav" | sudo tee /etc/systemd/system/clamav-daemon.service.d/extend.conf
sudo systemctl daemon-reload
sudo service clamav-daemon start
echo -e "#!/bin/sh\n/etc/init.d/clamav-freshclam stop\n/usr/bin/freshclam -v >> /var/log/clamav/freshclam.log\n/etc/init.d/clamav-freshclam start" | sudo tee /etc/cron.daily/freshclam
sudo chmod +x /etc/cron.daily/freshclam

# Reload systemd to apply changes
sudo systemctl daemon-reload

crontab -e
@reboot /usr/bin/python3 /path/to/your/script.py

sudo apt-get install -y onboard

# Configure onboard to start when a text input area is focused
gsettings set org.gnome.desktop.a11y.applications screen-keyboard-enabled true
gsettings set org.gnome.settings-daemon.peripherals.keyboard numlock-state 'on'

echo "Onboard installed and configured. Restart your session or reboot for changes to take effect."

# Display completion message
echo "ClamAV installation and configuration completed."