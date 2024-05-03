#!/usr/bin/env bash

# check if Nginx is installed
if !nginx -v; then
	sudo apt -y update
	sudo apt install -y nginx
fi

# create folder /data/
if [ ! -d "/data"]; then
	sudo mkdir /data/
fi

# create folder /data/web_static/
if [ ! -d "/data/web_static/"]; then
        sudo mkdir /data/web_static/
fi

# create folder /data/web_static/releases/
if [ ! -d "/data/web_static/releases/"]; then
        sudo mkdir /data/web_static/releases/
fi

# create folder /data/web_static/shared/
if [ ! -d "/data/web_static/shared/"]; then
        sudo mkdir /data/web_static/shared/
fi

# create /data/web_static/releases/test/
if [ ! -d "/data/web_static/releases/test/"]; then
        sudo mkdir /data/web_static/releases/test/
fi

# fake html file for testing 
echo "<html>
  <head>
  </head>
  <body>
    <h1> Derrick Muturi vs Nginx </h>
  </body>
</html>" | sudo tee "/data/web_static/releases/test/index.html" > /dev/null

# create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership of /data/ folder to the ubuntu us/data/web_static/currenter
sudo chown -R ubuntu: ubuntu/data

#update Nginx config to serve content of /data/web_static/current/ to hbnb_static
if [ -e "/etc/nginx/sites-available/default_backup" ]; then
       sudo cp /etc/nginx/sites-available/default_backup /etc/nginx/sites-available/default
else
       sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default_backup
fi
sed -i "0,/location \/ {/s||location \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}\n\n\t&|" /etc/nginx/sites-available/default

sudo service nginx restart
