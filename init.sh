#!/bin/bash

#./key_authority.py &>/dev/null &
#mosquitto -c mosquitto.conf &>/dev/null &

./key_authority.py &
/usr/sbin/mosquitto -c mosquitto.conf &

printf "Key Authority server inicio\n"
printf "Mosquitto server inicio\n"

exit 0
