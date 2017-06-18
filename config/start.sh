#!/bin/sh

sudo certbot certonly --webroot --webroot-path=/opt/reflection/data/webroot -d mihalea.ro -d www.mihalea.ro 
sudo openssl dhparam -out /etc/letsencrypt/live/mihalea.ro/dhparam.pem 2048
echo -e "ADD TO SUDO CRONTAB:
15 3 19 * *  /opt/reflection/config/renew.sh" 
