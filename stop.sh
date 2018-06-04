#!/bin/bash

# Stop our docker container
docker stop $(docker ps -q)
