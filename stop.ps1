# This file serves the same purpose as stop.sh, but should now run
# in Windows Powershell

#Stops docker container
$imagesToStop = docker ps -q
docker stop $imagesToStop
