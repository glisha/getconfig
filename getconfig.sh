#!/bin/bash

#crontab example
#49 5 * * * /home/fetchconfig/sshfetch/getconfig.sh > /dev/null 2>&1

cd /home/fetchconfig/sshfetch/
./getconfig.py
