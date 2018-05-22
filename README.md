# ask-meagain

ALOT of work needs to be done here, and this is about as basic as it can get, but here's a starting place
To run the application you need to:

1.) Install docker, then clone the repo
2.) (One of the early steps will be to create scripts for this process) Build the docker project
  "docker build -t name ."
3.) Run the newly built image
  "docker run -p 7697:80 name"

You should now be running the application locally on localhost:7697

---Some more notes---
Currently, the conf folder takes no effect
Built using notes on the Docker image page: https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/
To add nginx configurations, Dockerfile modifications need to be made, copy .conf files to /etc/nginx/conf.d/
