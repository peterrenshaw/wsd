#!/bin/sh


#=======
# name: cron.sh
# date: 2018OCT31
# prog: pr
# desc: Weather Report cron setup
# usge: 
#       sudo ./cron.sh
# 
#       disable the emails
#           >/dev/null 2>&1
#========


{
    USR=pr
    CTP=/Users/pr/work/code/py/wsd/conf/crontab.cron

    echo "REMEMBER SUDO"
    echo "User: $USR"
    echo "Cron: $CTP"

    crontab -u $USR $CTP
    crontab -l


}
>/dev/null 2>&1
