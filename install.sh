#!/bin/bash
apt-get install python3
D1='/data/data/com.termux/files/usr/bin'
nm='tdwnsv3'

if [[ -d  "$D1" ]]; then
    DIR="$D1"
else
    DIR='/usr/bin'
fi 

python3 setup.py install

ex="$DIR"/"$nm"

cp main.py "$ex"

chmod +x "$ex"

echo "$nm" 'installed successfully!'

sleep 2 && clear

tdwnsv3 -v && tdwnsv3 -h
