#!/bin/bash
# To be run on host machine to start up docker container

# Define variables
imageName="script-build"
check=`docker image ls | grep $imageName | cut -d' ' -f27`

#Check for docker image, if not, build it
if [ $check ]
then
  echo "Docker build already exists"
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
