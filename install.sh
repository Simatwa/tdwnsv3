#!/bin/bash
apt-get install python3

nm='tdwnsv3'

python3 setup.py install

echo "$nm" 'installed successfully!'

sleep 2 && clear

tdwnsv3 -v && tdwnsv3 -h
