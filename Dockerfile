FROM python:3.9
RUN apt update -y && \
    apt install telnet -y && \
    rm -rf var/lib/apt/lists/*

RUN mkdir /data-copier
COPY ./app /data-copier/app
COPY requirements.txt /data-copier

RUN pip install -r /data-copier/requirements.txt