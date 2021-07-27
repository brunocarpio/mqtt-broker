#!/bin/bash

mkdir charm-install && cd charm-install
curl -LO https://raw.githubusercontent.com/brunocarpio/charm-install-script/main/script.sh && bash script.sh
cd ../ && sudo rm -rf charm-install

sudo apt install --yes mosquitto
sudo systemctl disable mosquitto && sudo systemctl stop mosquitto
