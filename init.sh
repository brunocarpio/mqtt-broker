#!/bin/bash

#python3 key_authority.py &>/dev/null &
#mosquitto -c mosquitto.conf &>/dev/null &

python3 key_authority.py &
mosquitto -c mosquitto.conf &

printf "Key Authority server inicio\n"
printf "Mosquitto server inicio\n"

exit 0
