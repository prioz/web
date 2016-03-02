sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/etc/gunicorn.conf /etc/gunicorn.d/test
sudo /etc/init.d/nginx restart
gunicorn -c /etc/gunicorn.d/hello.py hello:wsgi_application
