server {
    {{ if not .ssl }}
    listen 80 default_server;
    {{ else }}
    listen 80 default_server ssl http2;
    {{ end }}


    include /etc/nginx/includes/server_params.conf;
    include /etc/nginx/includes/proxy_params.conf;

    {{ if .ssl }}
    include /etc/nginx/includes/ssl_params.conf;

    ssl_certificate /ssl/{{ .certfile }};
    ssl_certificate_key /ssl/{{ .keyfile }};
    {{ end }}



    location /api {
        proxy_pass http://backend;
        proxy_set_header Host $host;  
        proxy_set_header X-Real-IP $remote_addr;
    }

    #location /app {
    #    proxy_pass http://backend;
    #    proxy_set_header Host $host;  
    #    proxy_set_header X-Real-IP $remote_addr;
    #}

    location / {
        #allow   172.30.32.2;
        #deny    all;
        
        proxy_pass http://backend;
        
        proxy_set_header Host $host;  
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    #location / {
    #    try_files $uri $uri/ /index.html;
    #    proxy_http_version 1.1;
    #   proxy_set_header Upgrade $http_upgrade;
    #    proxy_set_header Connection "upgrade";
    #    proxy_set_header Host $host;
    #}
  
    location ~* /web/assets/.+\.js$ {
	    proxy_pass http://backend;
        proxy_set_header Host $host;  
        proxy_set_header X-Real-IP $remote_addr;
    }

    location ~* /web/assets/.+\.css$ {
        proxy_pass http://backend;
        proxy_set_header Host $host;  
        proxy_set_header X-Real-IP $remote_addr;
    }

}