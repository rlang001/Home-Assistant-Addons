
Fix ingress



server {
  listen 80 default_server;
  listen [::]:80 default_server;
  server_name _;
  proxy_max_temp_file_size 0;
  root /app/web/dist;

  location /api {
    proxy_pass http://0.0.0.0:8089;
    proxy_set_header Host $host;  
    proxy_set_header X-Real-IP $remote_addr;
  }

  location /openobserve {
    return 302 /openobserve/;
  }

  location /openobserve/ {
    proxy_pass http://0.0.0.0:5080;
    proxy_set_header Host $host;  
    proxy_set_header X-Real-IP $remote_addr;
  }

  location / {
    try_files $uri $uri/ /index.html;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Host $host;
  }

  location ~* /openobserve/web/assets/.+\.js$ {
    proxy_pass http://0.0.0.0:5080;
    proxy_set_header Host $host;  
    proxy_set_header X-Real-IP $remote_addr;
  }
  location ~* /openobserve/web/assets/.+\.css$ {
    proxy_pass http://0.0.0.0:5080;
    proxy_set_header Host $host;  
    proxy_set_header X-Real-IP $remote_addr;
  }

}