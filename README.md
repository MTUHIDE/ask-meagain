# ask-meagain

ALOT of work needs to be done here, and this is about as basic as it can get, but here's a starting place
To run the application you need to:

1. Install docker
2. Make sure the docker daemon is up and running
3. Clone the repo
4. Run the "start.sh" script (as root) to start running the docker container

You should now be running the application locally on localhost:7697

### Docker Container Notes
Docker is confusing, and hopefully once we get it right we won't have to mess with it much/at all. Some helpful hints for messing around with our containers below. All commands should be run in a bash shell.

* Add the flag "-r" on the start script to rebuild the image before running the container Example: `# bash start.sh -r`
  * You gotta stop the container to use the rebuild tag on start.sh
* Stop the container with `# bash stop.sh`
* View all running containers: `# docker ps`
  * To view all containers on the system `# docker ps -a`
  * To view all docker images on the system `# docker image ls -a`
* (Coming soon) To completely clean up everything docker has cached on your system, run: `# bash nukedocker.sh`


### ---Some more notes---
* Currently, the conf folder takes no effect
* Built using notes on the Docker image page [here](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/ "Image Documentation")
* To add nginx configurations, Dockerfile modifications need to be made, copy .conf files to /etc/nginx/conf.d/
