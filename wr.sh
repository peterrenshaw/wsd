#!/bin/sh


#=======
# name: wr.sh
# date: 2018OCT31
# prog: pr
# desc: Weather Report called via crontab.cron, calls ws.py twice
# 
#           a) GET latest report
#           ./ws.py -g 
#   
#           b) EXTRACT and simplifiy
#           ./ws.py -e
#
#       DATA FILES
#       the data files 'latest-weather-simple' and 'latest-weather-complex' 
#       are sent to the directory where d3js can access either by URL or FS.
#  
#       CRON TIMING
#       the weather service updates this report every 30min
#       so either a 45min update or 30min at 5min offset from 
#       the hour is ideal.
#
#       TODO
#
# usag: will show up in console via cron with the below echos
#       errors will be mailed
#=======


{
    #--------
    # SETUP
    #
    # application
    PYVER=python3
    #
    # production or testing?
    #
    TRUE=1
    FALSE=0
    IS_PROD=$TRUE
    #
    # prod information
    #
    PRODUCT_NAME='weather service data'
    SCRIPT_NAME='WSD'
    #--------

    #--------
    # PATHS
    # depending on linux (production) or mac (development)
    LIN_USER=pi
    LIN_HOME=/home/$LI_USER/code
    MAC_USER=pr
    MAC_HOME=/Users/$MAC_USER/work/code
    CODEDIR='wsd'
    #
    # build filepath, machine dependent
    #
    if [ "$IS_PROD" = "$TRUE" ]; then
        CODE_PATH=$LIN_HOME/$CODEDIR
    else
        CODE_PATH=$MAC_HOME/$CODEDIR
    fi
    #--------


    #--------
    # EXECUTE
    # this is what is called every time cron is called
    echo "$SCRIPT_NAME start"
    PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin
    $PYVER $CODE_PATH/wsd.py -g
    $PYVER $CODE_PATH/wsd.py -e
    echo "$PRODUCT_NAME called"
    echo "$SCRIPT_NAME stop"
    #--------
} >&2
