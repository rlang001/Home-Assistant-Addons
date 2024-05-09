ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apt-get update && apt-get -y upgrade

#########################################################
# Install prerequisites
#########################################################

# RUN apt-get install -y wget git python3 python3-venv libgl1 libglib2.0-0

#WORKDIR /root
#RUN wget -q https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui/master/webui.sh

# RUN git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git


#########################################################
# Remove nginx config, temp stuff
#########################################################
RUN rm -fr \
      /etc/nginx \
      /tmp/*

#########################################################
# Copy data for add-on to docker fs
#########################################################
COPY rootfs /

#########################################################
# 
#########################################################
COPY run.sh /
RUN chmod 777 /run.sh
CMD [ "/run.sh" ]