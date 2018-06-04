FROM tiangolo/uwsgi-nginx-flask:python3.6

ENV STATIC_URL /static
ENV STATIC_PATH /app/app/static

COPY ./app /app
