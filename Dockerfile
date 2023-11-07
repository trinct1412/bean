FROM python:3.10.7-alpine

RUN apk add --update alpine-sdk


#create folder
RUN mkdir /src && mkdir -p /.cache/pip && mkdir -p /.local && chmod -R 777 /.cache && chmod -R 777 /src && chmod -R 777 /.local
#set Directory
WORKDIR /src

ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/.local/bin

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /src/

RUN chown -R 1000:1000 /src/

USER 1000
RUN chmod +x /src/entrypoint.sh
