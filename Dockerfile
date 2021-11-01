FROM python:3.7

ENV PYTHONBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

RUN mkdir /app
COPY . /app
WORKDIR /app