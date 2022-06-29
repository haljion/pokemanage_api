FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /src
WORKDIR /src

RUN apt-get -y update \
    && apt-get install -y \
    git
RUN pip install --upgrade pip

COPY ./requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt
ADD . /src/

RUN mkdir -p /var/run/gunicorn

# docker container exec -it db psql -U postgres
# CREATE DATABASE pokemanage;
# CREATE USER admin WITH PASSWORD 'password';
# GRANT ALL PRIVILEGES ON DATABASE pokemanage TO admin;