#!/bin/bash

#
# This script will check if any changes have been made
# to the Nagios files in the last 24 hours, and if so,
# will do a git add, commit, and push to gitlab.
#
# Created Jan 22, 2022 - IneptTech.com
#

# Changes to the Nagios LLAC config directory
cd /opt/nagios

# Gets the location of the bin file
gitbin=`which git`

# Location of the repo
repo_dir="/opt/nagios"

# URL of the repo
git_repo=https://github.com/inepttech/nagios-backup.git

# Branch of the repo
current_branch=$(git branch | grep "*" | cut -b 3-)

# Get's todays date and formats YYYYMMDD
# as well as echo's the date for the log file
todays_date=`date +"%Y%m%d %I:%M%P"`
echo $todays_date

# Compares the saved GIT URL to the repo URL before pushing
git_repo_check=`git config --get remote.origin.url`

if [ "$git_repo_check" == "$git_repo" ]; then
    # If everything is good, git will add, commit, and push
    ${gitbin} add -A
    ${gitbin} commit -m "Auto Backup - $todays_date"
    ${gitbin} push origin $current_branch
else
    # If there's an error, the script will exit
    exit 0
fi

# Add task completed text for log file and exit script
printf "Task completed. Exiting \n\n"
exit 0
