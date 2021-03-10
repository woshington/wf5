FROM python:3
LABEL maintainer="woshingtonvaldeci@gmail.com"
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt