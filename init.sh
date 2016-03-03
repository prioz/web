#!/bin/bash

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql restart
cd ~/web && gunicorn -D -c /etc/gunicorn.d/hello.py hello:wsgi_application
cd ~/web/ask && gunicorn -D -c /home/box/web/etc/ask.py ask.wsgi
#sudo nano /var/log/nginx/error.log
#sudo nano /var/log/nginx/access.log
