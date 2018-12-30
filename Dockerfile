FROM frolvlad/alpine-python-machinelearning
RUN apk add --no-cache bash

ENV LANG C.UTF-8
ENV APP_HOME /scripts
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
ADD . $APP_HOME
RUN pip install -r ./requirements.txt