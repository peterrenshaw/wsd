#!/bin/sh


#=======
# name: cron.sh
# date: 2018OCT31
# prog: pr
# desc: Weather Report cron setup
# 
#           a) GET latest report
#           sudo ./cron.sh
# 
#========


{
    USER=pr
    CODE=/User/pr/work/code/py/wsd/wr.sh

    echo "REMEMBER SUDO"
    crontab -u $USER $CODE
    echo 'crontab -u' $USER $CODE
    crontab -l

} >&2
