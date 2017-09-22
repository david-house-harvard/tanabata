FROM python:3.6-alpine3.6
MAINTAINER maksim.sokolskiy@raccoongang.com
ENV PYTHONUNBUFFERED 1
RUN  apk update && apk add alpine-sdk
RUN mkdir /tanabata
WORKDIR /tanabata
ADD requirements.txt /tanabata/requirements.txt
RUN pip install -r requirements.txt
