# ask-meagain

This is legacy code for using askmeagain with flask, we have no moved to Django and are developing with that.


ALOT of work needs to be done here, and this is about as basic as it can get, but here's a starting place
To run the application you need to:

1. Install docker
2. Make sure the docker daemon is up and running
3. Clone the repo
4. Run the "start.sh" script (as root) to start running the docker container

You should now be running the application locally on localhost:7697

### Docker Container Notes
Docker is confusing, and hopefully once we get it right we won't have to mess with it much/at all. Some helpful hints for messing around with our containers below. All commands should be run in a bash shell.

* Stop the container with `# bash stop.sh`
* View all running containers: `# docker ps`
  * To view all containers on the system `# docker ps -a`
  * To view all docker images on the system `# docker image ls -a`
* Fan of the Youtube Channel, "Whats Inside"? Use `# docker exec -it <container-ID or name> /bin/bash` to open a shell inside our container

### Specific Notes for start.sh
Alot of modifications have been made to start.sh since it existed as just a "docker run" command, so I'm listing how to use it here.

* To get up and running for development as fast as possible: `# bash start.sh`
    * This will start the container while mounting your local ./app directory to the container's /app directory. This allows for real time code changes to take place in the app with just a refresh. In order to make this work, uwsgi has to be cut out (done for you) and the flask app run directly from python, so the end result means it won't be running in exactly production mode.
* To run in production mode use the tag: `-l` or `--legacy`
    * This is what should be used to deploy for full application testing, and runs the app through the correct pipeline (flask -> uwsgi -> nginx)
* To rebuild the container (if you make non-python related changes), use this tag: `-r`
    * I expect almost no-one will ever have to use this, but you never know
* Please use only one tag at a time :)

### SQL/DB Notes
* Sqlite3 support has now been added via SQLAlchemy. Documentation on how to use SQLAlchemy here: http://flask-sqlalchemy.pocoo.org/2.3/
* Bootstrapped test data coming soon

### ---Some more notes---
* Currently, the conf folder takes no effect
* Built using notes on the Docker image page [here](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/ "Image Documentation")
* To add nginx configurations, Dockerfile modifications need to be made, copy .conf files to /etc/nginx/conf.d/
