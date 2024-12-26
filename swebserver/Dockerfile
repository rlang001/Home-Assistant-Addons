
ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apt-get update && apt upgrade -y

#########################################################
# Install prerequisites
#########################################################
RUN apt-get update
RUN apt-get install -y wget nginx 

#########################################################
# Development stuff.  Not needed for operation
#########################################################
RUN apt-get update
RUN apt-get install -y vim 

# Copy root filesystem
COPY rootfs /

#WORKDIR /var/www/html/script
#RUN wget https://unpkg.com/grapesjs

#WORKDIR /var/www/html/css
#RUN wget https://unpkg.com/grapesjs/dist/css/grapes.min.css


COPY run.sh /
RUN chmod 777 /run.sh
CMD [ "/run.sh" ]