## 0x10. HTTPS SSL
steps to install cerbot certificate for a HTTP website is running HAproxy on Ubuntu 20

sudo snap install core; sudo snap refresh core

sudo apt-get remove certbot

sudo snap install --classic certbot

sudo ln -s /snap/bin/certbot /usr/bin/certbot

sudo service haproxy stop

sudo certbot certonly --webroot

sudo mkdir -p /etc/ssl/www.example.tech

sudo cat /etc/letsencrypt/live/www.example.tech/fullchain.pem /etc/letsencrypt/live/www.example.tech/privkey.pem | sudo tee /etc/ssl/www.example.tech/www.example.tech.pem

vim /etc/haproxy/haproxy.cfg

in the file you must have :

frontend www-http

        bind *:80
        default_backend web-backend
        bind *:443 ssl crt /etc/ssl/www.example.tech/www.example.tech.pem
        redirect scheme https code 301 if !{ ssl_fc }
backend web-backend

        balance roundrobin
        server xxxx-web-01 ip_server:80 check
        server xxxx-web-02 ip_server:80 check

sudo service haproxy restart

if you have a problem you can do the command haproxy -f /etc/haproxy/haproxy.cfg -db to see what happen

