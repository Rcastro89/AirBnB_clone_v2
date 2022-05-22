#!/usr/bin/env bash
# Configura los servidores web para la implementación de web_static.


sudo apt-get update
sudo apt-get install -y nginx
sudo service nginx start
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data
sed -i '/listen 80 default_server;/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart
