#!/bin/bash
# This script will backup the Documents folder. Paired with a launchd process, it will run at midnight every night, or whenever the computer next starts up. It does not sync the directory every time a file is changed, but that is something to look into.
if ! pgrep -x rsync > /dev/null ; then
    rsync -hvrltD --modify-window=1 --delete --log-file=~/backup.log ~/Documents /Volumes/G_DRIVE/MacBook_Air
fi
