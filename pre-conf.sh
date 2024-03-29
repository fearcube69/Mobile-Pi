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

sudo apt-get install psmisc
#crontab -e
#@reboot /usr/bin/python3 /path/to/your/script.py

sudo apt-get install -y matchbox-keyboard

# Install xdotool
sudo apt-get install -y xdotool

# Configure Matchbox keyboard to start when a text input area is focused
mkdir -p ~/.config/autostart
echo -e "[Desktop Entry]\nType=Application\nName=Matchbox Keyboard\nExec=matchbox-keyboard\n" > ~/.config/autostart/matchbox-keyboard.desktop

echo -e "#!/bin/bash\nmatchbox-keyboard &" > ~/start_matchbox_keyboard.sh
chmod +x ~/start_matchbox_keyboard.sh

# Create a .desktop file for autostart
echo -e "[Desktop Entry]\nType=Application\nExec=/home/pi/start_matchbox_keyboard.sh\nHidden=false\nNoDisplay=false\nX-GNOME-Autostart-enabled=true\nName=MatchboxKeyboard" > ~/.config/autostart/matchbox-keyboard.desktop

echo "Matchbox keyboard installed and configured. Restart your session or reboot for changes to take effect."

# on boot config when starting up

SCRIPT_NAME="Main.py"
BUILD_DIR="build"
CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
RC_LOCAL="/etc/rc.local"

# Check if the script name is provided
if [ -z "$SCRIPT_NAME" ]; then
    echo "Error: Please provide the name of your Python script."
    exit 1
fi

# Add the script execution command to rc.local
sudo sed -i -e '$i \sudo python3 '"$CURRENT_DIR/$BUILD_DIR/$SCRIPT_NAME"' &\n' "$RC_LOCAL"




# Define the file path
desktop_file="$HOME/.config/autostart/startup.desktop"

# Check if the directory exists, if not, create it
mkdir -p "$HOME/.config/autostart"

# Create the desktop file
cat <<EOL > "$desktop_file"
[Desktop Entry]
Type=Application
Name=Startup Script
Exec=python3 /home/mopi/Mobile-Pi/build/Main.py
X-GNOME-Autostart-enabled=true
EOL

# Make the desktop file executable
chmod +x "$desktop_file"

echo "Desktop file created at: $desktop_file"
echo "Restart to see change."



echo "Configuration complete. Reboot your Raspberry Pi to start the script on boot."
# Display completion message
echo "ClamAV installation and configuration completed."


# Install Matchbox Keyboard
sudo apt install matchbox-keyboard
sudo apt-get install libmatchbox1 -y

# Create a script to toggle the Matchbox keyboard
echo '#!/bin/bash
PID="$(pidof matchbox-keyboard)"
if [ "$PID" != "" ]; then
 kill $PID
else
 matchbox-keyboard &
fi' | sudo tee /usr/bin/toggle-keyboard.sh > /dev/null

# Give execute permissions to the script
sudo chmod +x /usr/bin/toggle-keyboard.sh

# Create a desktop entry file for the Matchbox keyboard
echo '[Desktop Entry]
Name=Toggle Matchbox Keyboard
Comment=Toggle Matchbox Keyboard
Exec=toggle-keyboard.sh
Type=Application
Icon=matchbox-keyboard.png
Categories=Panel;Utility;MB
X-MB-INPUT-MECHANSIM=True' | sudo tee /usr/share/applications/toggle-keyboard.desktop > /dev/null


# Set up the keyboard to auto-start when the Raspberry Pi boots up
echo 'toggle-keyboard.sh' >> ~/.bashrc