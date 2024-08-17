#!/bin/bash
# This script will backup the Documents folder. Paired with a launchd process, it will run at 
# midnight every night, or whenever the computer next starts up.
if ! pgrep -x rsync > /dev/null ; then
    touch '/Users/davidmeixner/Documents/.timestamp'
    touch '/Users/davidmeixner/Pictures/.timestamp'
    echo "Start:" `date` > /Users/davidmeixner/backup.log
    rsync -hvrltD --modify-window=1 --delete-during "/Users/davidmeixner/Documents" "/Volumes/G_DRIVE/MacBook_Air"
    rsync -a "/Users/davidmeixner/Pictures" "/Volumes/G_DRIVE"
    echo "  End:" `date` >> /Users/davidmeixner/backup.log
fi
