#!/bin/bash
D1='/data/data/com.termux/files/usr/bin'

if [[ -d  "$D1" ]]; then
    DIR="$D1"
else
    DIR='/usr/bin'
fi  

if [[ -f "$DIR"/python ]]; then
      python setup.py sdist

else
      apt-get install python3
      python3 setup.py sdist
fi 

cp main.py "$DIR"/tdwnsv3

chmod +x "$DIR"/tdwnsv3

echo 'tdwnsv3 installed successfully!'

sleep 2 && clear

tdwnsv3 -v && tdwnsv3 -h