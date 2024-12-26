ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apt-get update && apt-get -y upgrade

RUN apt-get install -y libusb-1.0-0 wget

# Install Go
WORKDIR /root
RUN wget https://go.dev/dl/go1.23.1.linux-amd64.tar.gz

RUN rm -rf /usr/local/go && tar -C /usr/local -xzf /root/go1.23.1.linux-amd64.tar.gz
RUN export PATH=$PATH:/usr/local/go/bin

RUN go install github.com/bemasher/rtlamr@latest


#########################################################
COPY rootfs /

#########################################################
COPY run.sh /
RUN chmod 777 /run.sh
CMD [ "/run.sh" ]
