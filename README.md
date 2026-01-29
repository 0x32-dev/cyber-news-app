# Cybersecurity News Web App 

An application made in Flask to pull RSS feeds into one site.

*Important Notice: This build assumes you have already generated your certifcates

## Deployment 
* Clone the repository:
```
git clone https://github.com/0x32-dev/cyber-news-app.git
```

* Create Nginx.conf
Make the directory:
```
mkdir ngnix
```

Then create the configuration file:


```
server {
    listen 80;
    server_name $DOMAIN;

    # Redirect all HTTP to HTTPS
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name $DOMAIN;

    ssl_certificate /etc/letsencrypt/live/$DOMAIN/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/$DOMAIN/privkey.pem;

    location / {
        proxy_pass http://flask:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

```
* Install docker & docker compose
```
sudo apt install docker && docker-compose
```

* Run containers
```
sudo docker-compose up -d --build
```
 
