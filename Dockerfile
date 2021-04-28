FROM ubuntu:latest

MAINTAINER "antishipul@gmail.com"

# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

# install python
RUN apt-get update                    \
    && apt-get install -y python3-pip \
    && cd /usr/local/bin              \
    && ln -s /usr/bin/python3 python

# install additionals
RUN apt-get update          \
    && apt-get install -y   \
    apt-utils bash vim curl \
    git gcc

# install pip
RUN curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py

COPY . project

# install requirements
RUN pip3 install --upgrade pip
RUN rm -rf $HOME/.cache/pip3/*
RUN pip3 install virtualenv
RUN virtualenv venv
RUN chmod -R 775 venv/bin/
RUN venv/bin/activate
RUN pip3 install -r project/requirements.txt

# delete python build cache
RUN find project/ -name \*.pyc -delete

# delete previouse log files
RUN rm -f -R logs/

RUN pwd && ls -la

VOLUME ["./allure_/allure_results"]

WORKDIR project

# set display port to avoid crash
ENV DISPLAY=:99
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null

# Leave it on
CMD tail -f /dev/null
