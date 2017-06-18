#!/bin/sh

sudo certbot certonly --webroot --webroot-path=/opt/reflection/data/webroot -d mihalea.ro -d www.mihalea.ro
sudo openssl dhparam -out /etc/letsencrypt/live/mihalea.ro/dhparam.pem 2048

15 3 19 * *  /usr/bin/certbot renew --quiet --renew-hook "cd /opt/reflection && docker-compose restart"
