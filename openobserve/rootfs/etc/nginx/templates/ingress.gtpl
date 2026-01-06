server {
    listen {{ .interface }}:{{ .port }}  default_server;


    include /etc/nginx/includes/server_params.conf;
    include /etc/nginx/includes/proxy_params.conf;
    


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
  
#   location /web/ {
        proxy_pass http://backend;
#       proxy_set_header Host $host;  
#       proxy_set_header X-Real-IP $remote_addr;
#    }

    location ~* /web/src/assets/.+\.js$ {
        proxy_pass http://backend;
        proxy_set_header Host $host;  
        proxy_set_header X-Real-IP $remote_addr;
    }


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