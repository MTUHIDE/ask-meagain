# This file serves the same purpose as start.sh, but should now run
# in Windows Powershell

$imageName = "script-build"

# TODO: add some checking for previous builds down the road

# Build image
# Right now this will build every time
Write-Host "Deleting and Rebuilding Docker Image"

$imageToDel = docker image ls -q
docker rmi -f $imageToDel

docker build -t ask:$imageName .

# Time to run our build
Write-Host "Running docker container built above"
docker run -d -p 7697:80 ask:$imageName
