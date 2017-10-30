#!/bin/sh
cd Photos
echo "Taking the Photo"
now=$1 #Now is the filename time stamp
#take pic
fswebcam --no-banner -d /dev/video0 $now.jpg
echo "Picture Taken"
echo ""

