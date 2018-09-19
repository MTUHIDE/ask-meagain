#!/bin/bash
# To be run on host machine to start up docker container
# IMPORTANT NOTES BELOW
#   It's best to run this from the source directory. Not doing this can cause
#       problems
#   Running with -r will stop your docker instance, then rebuild and start it

# Define variables
imageName="script-build"
check=`docker image ls | grep $imageName | cut -d' ' -f27`

#Check for docker image, if not, build it
if [ $check ]
then
  echo "Docker build already exists"
  if [[ $1 == "-r" ]] # Checking for "-r" flag - rebuild the project
  then
    echo "Checking to make sure docker is stopped"
    if [ `docker ps -q` ]
    then
        echo "Docker is running, stopping docker now"
        ./stop.sh
    fi
    echo "Rebuilding docker image"
    docker rmi -f $(docker image ls -q)
    docker build -t ask:$imageName .
  fi
else
  echo "Creating docker build"
  docker build -t ask:$imageName .
fi

#Make it look like the script is doing something
echo " "
sleep 1

# Run docker container from above image
echo "Running docker container built above"
docker run -d -p 7697:80 ask:$imageName
