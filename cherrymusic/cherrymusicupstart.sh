#!/bin/bash

#put in: usr/bin/local/

echo "Starting Cherrymusic server at port 7600"

screen -d -m python /opt/cherrymusic/cherrymusic

#make executable: chmod 744 /esr/local/bin/cherrymusicupstart.sh
