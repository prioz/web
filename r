#!/bin/bash

cd ~
rm -rf web
git clone https://github.com/prioz/web /home/box/web
bash /home/box/web/init.sh
