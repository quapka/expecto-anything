#!/usr/bin/env bash

virtualenv_cmd=virtualenv
VIRTUAL_DIR=virtual
python=python3

proper_environment=true

# shellcheck disable=I1117
RED="\033[1;31m"
GREEN="\033[1;32m"
NOCOLOR="\033[0m"

# helper functions for nicer prints
function green {
    echo "$GREEN$1$NOCOLOR"
}

function red {
    echo "$RED$1$NOCOLOR"
}

echo "Checking the presence of a '$virtualenv_cmd'.."
if ! "$virtualenv_cmd" --version > /dev/null; then
    echo "[Error] You are missing '$virtualenv_cmd'. Try using a package manager to install it."
    proper_environment=false
else
    echo "[ OK ] '$virtualenv_cmd' exists!"
fi

echo "Checking the presence of a '$python'.."
if ! "$python" --version > /dev/null; then
    echo "[Error] You are missing '$python'. Try using a package manager to install it."
    proper_environment=false
else
    echo "[ OK ] '$python' exists!"
fi

echo "Checking the presence of a '$VIRTUAL_DIR' directory.."
if [ -d "$VIRTUAL_DIR" ]; then
    echo "Error: The directory '$VIRTUAL_DIR' already exists. Remove it and try again."
    proper_environment=false
else
    echo "[ OK ] '$VIRTUAL_DIR' does not exist yet."
fi


if [ "$proper_environment" != true ]; then
    echo "Environment check: FAILED!"
    # red FAILED
    echo "Your environment is not setup properly."
    exit 1
fi


echo
echo "Environment check: PASSED!"

echo "Creating the virtual environment:"
"$virtualenv_cmd" "--python=/usr/bin/$python" "virtual"

# echo "Sourcing the virtual environment:"
# export source "$VIRTUAL_DIR/bin/activate"

# echo "Updating the virtual environment:"
# pip install -r "requirements.txt"
echo
echo
echo "You are almost good to go!"
echo
echo "To activate the virtual environment run:"
echo "$ source $VIRTUAL_DIR/bin/activate"
echo
echo "To update it with the necessary packages run:"
echo "$ pip install -r requirements.txt"
echo
echo "Finally, to run the project:"
echo "$ python spacex_launch_alarm.py -m your-favorite-music.mp3"

