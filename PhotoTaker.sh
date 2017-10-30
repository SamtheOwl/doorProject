#!/bin/sh
cd Photos
echo "Taking the Photo"
currentTime=$1
fswebcam --no-banner -d /dev/video0 $currentTime.jpg
echo "Picture Taken"
echo ""
