#!/bin/bash

#This script looks for a bluetooth audio source and launch the pulse audio loopback module if necessary

#log traces :
#date=$(date "+%Hh%Mm%Ss")
#echo "Script Exec "$date

bluetoothSource=$(pactl list sources short | grep bluez_source)

read loopbackStatus < /root/bluetoothLoopbackStatus.txt

if [[ $bluetoothSource != "" ]] && [[ $loopbackStatus == "0" ]]
then
   source=${bluetoothSource:2:30}
   pactl load-module module-loopback source=$source sink=alsa_output.0.analog-stereo
   echo "1" > /root/bluetoothLoopbackStatus.txt
   #echo "command launched"

else
   if [[ $bluetoothSource == "" ]] && [[ $loopbackStatus == "1" ]]
   then
      echo "0" > /root/bluetoothLoopbackStatus.txt
      #echo "reset loopbackStatus"
   fi
fi
