#!/bin/sh

/usr/bin/certbot renew --quiet --renew-hook "cd /opt/reflection && docker-compose restart"
cp /etc/letsencrypt/live/mihalea.ro/{fullchain,privkey,dhparam}.pem /opt/reflection/config/certs/
