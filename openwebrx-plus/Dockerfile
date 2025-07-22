ARG BUILD_FROM
FROM $BUILD_FROM

ENV TZ=UTC


RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y software-properties-common gpg rtl-sdr librtlsdr0 librtlsdr-dev expect

# OpenWebRX install keys/sources
RUN curl -s https://luarvique.github.io/ppa/openwebrx-plus.gpg | gpg --dearmor -o /etc/apt/trusted.gpg.d/openwebrx-plus.gpg
RUN tee /etc/apt/sources.list.d/openwebrx-plus.list <<<"deb [signed-by=/etc/apt/trusted.gpg.d/openwebrx-plus.gpg] https://luarvique.github.io/ppa/debian ./"
RUN curl -s https://repo.openwebrx.de/debian/key.gpg.txt | gpg --yes --dearmor -o /usr/share/keyrings/openwebrx.gpg
RUN tee /etc/apt/sources.list.d/openwebrx.list <<<"deb [signed-by=/usr/share/keyrings/openwebrx.gpg] https://repo.openwebrx.de/debian/ bullseye main"
RUN apt-get update

RUN apt-get install -y openwebrx



#########################################################
# Copy data for add-on to docker fs
#########################################################
COPY rootfs /

########################################################
# Modify the existing /run.sh file
########################################################
COPY run.sh /
RUN chmod 777 /run.sh
CMD [ "/run.sh" ]