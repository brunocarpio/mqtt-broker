#!/bin/sh

mosquitto_pid=$(ps aux | grep "\smosquitto\s" | sed '' | sed 's/^[a-zA-Z]\++\s\+\([0-9]\+\)\s\+.*$/\1/')
ka_pid=$(ps aux | grep "\spython3\s" | sed 's/^[a-zA-Z]\+.\s\+\([0-9]\+\)\s\+.*$/\1/')

kill -9 $mosquitto_pid
kill -9 $ka_pid

printf "KA HTTP server fin\n"
printf "Mosquitto server fin\n"
