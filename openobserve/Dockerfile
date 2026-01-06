ARG BUILD_FROM
FROM $BUILD_FROM

# ENV LANG=C.UTF-8
ENV TZ=UTC


RUN apt-get update && apt-get -y upgrade

RUN   apt-get install -y \
    wget \
    pwgen \
    python3 \
    nginx \
    gpg \
    vim

    #libdbd-mysql \
    #mariadb-server \
    


# syslog-ng - get a specific version
RUN \
    wget -qO - https://ose-repo.syslog-ng.com/apt/syslog-ng-ose-pub.asc |  gpg --dearmor -o /etc/apt/keyrings/syslog-ng-ose.gpg && \
    echo "deb [signed-by=/etc/apt/keyrings/syslog-ng-ose.gpg] https://ose-repo.syslog-ng.com/apt/ stable debian-bookworm" | tee /etc/apt/sources.list.d/syslog-ng-ose.list > /dev/null && \
    apt-get update && \
    apt-get install -y syslog-ng-mod-http=4.10.2-1
    

WORKDIR /root
# Fix for other arch

# ARM64
# curl -L -o openobserve-ee-v0.30.2-linux-arm64.tar.gz https://downloads.openobserve.ai/releases/o2-enterprise/v0.30.2/openobserve-ee-v0.30.2-linux-arm64.tar.gz && tar -xzf openobserve-ee-v0.30.2-linux-arm64.tar.gz

# AMD64
RUN curl -L -o openobserve-ee-v0.30.2-linux-amd64.tar.gz https://downloads.openobserve.ai/releases/o2-enterprise/v0.30.2/openobserve-ee-v0.30.2-linux-amd64.tar.gz && tar -xzf openobserve-ee-v0.30.2-linux-amd64.tar.gz

RUN chmod +x openobserve

#########################################################
# Remove configs
#########################################################
RUN rm -fr \
    /etc/nginx \
    /etc/php \
    /etc/syslog-ng



#########################################################
# Copy data for add-on to docker fs
#########################################################
COPY rootfs /

RUN chmod 755 /etc/s6-overlay/s6-rc.d/init-nginx/run && \
    chmod 755 /etc/s6-overlay/s6-rc.d/init-syslog-ng/run && \
    chmod 755 /etc/s6-overlay/s6-rc.d/nginx/run && \
    chmod 755 /etc/s6-overlay/s6-rc.d/nginx/finish && \
    chmod 755 /etc/s6-overlay/s6-rc.d/openobserve/run && \
    chmod 755 /etc/s6-overlay/s6-rc.d/openobserve/finish && \
    chmod 755 /etc/s6-overlay/s6-rc.d/syslog-ng/run && \
    chmod 755 /etc/s6-overlay/s6-rc.d/syslog-ng/finish
    
    
    
#########################################################
# Run the run.sh script
#COPY run.sh /
#RUN chmod 777 /run.sh
# WORKDIR /
# CMD [ "/run.sh" ]
