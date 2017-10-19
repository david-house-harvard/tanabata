FROM leafney/alpine-selenium-chrome
MAINTAINER maksim.sokolskiy@raccoongang.com
ENV PYTHONUNBUFFERED 1
RUN  apk update && apk add alpine-sdk python-dev libffi-dev
RUN mkdir /tanabata
WORKDIR /tanabata
ADD requirements.txt /tanabata/requirements.txt
RUN pip install -r requirements.txt
