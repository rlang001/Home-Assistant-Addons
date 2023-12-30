ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apt-get update && apt-get -y upgrade

#########################################################
# Install prerequisites
#########################################################
RUN apt-get install -y wget gpg apt-transport-https expect

RUN wget -O - https://repo.openwebrx.de/debian/key.gpg.txt | gpg --dearmor -o /usr/share/keyrings/openwebrx.gpg
RUN echo "deb [signed-by=/usr/share/keyrings/openwebrx.gpg] https://repo.openwebrx.de/debian/ bullseye main" > /etc/apt/sources.list.d/openwebrx.list
RUN apt-get update
RUN apt-get install -y openwebrx


#########################################################
# Copy data for add-on to docker fs
#########################################################
COPY rootfs /

#########################################################
# Startup
# Right now weewx is started from run.sh
#########################################################
#COPY weewx.debian /etc/init.d/weewx
#RUN chmod +x /etc/init.d/weewx
#RUN update-rc.d weewx defaults 98

#########################################################
# 
COPY run.sh /
RUN chmod 777 /run.sh
CMD [ "/run.sh" ]