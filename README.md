# ask-meagain

ALOT of work needs to be done here, and this is about as basic as it can get, but here's a starting place
To run the application you need to:

1.) Install docker
2.) Clone the repo
2.) Run the "start.sh" script to start running the docker container

You should now be running the application locally on localhost:7697

To stop running the container, use "docker stop container-id"

---Some more notes---
Currently, the conf folder takes no effect
Built using notes on the Docker image page: https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/
To add nginx configurations, Dockerfile modifications need to be made, copy .conf files to /etc/nginx/conf.d/
