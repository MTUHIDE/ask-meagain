FROM tiangolo/uwsgi-nginx-flask:python3.6

ENV STATIC_URL /static
ENV STATIC_PATH /app/ask_meagain/static

COPY ./app /app

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y sqlite3 libsqlite3-dev
RUN pip install -e /app/ 
