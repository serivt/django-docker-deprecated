# Django - Docker
Production-ready Django project layout on Docker (Python 3)


## Install docker (Ubuntu 16.04)
```sh
sudo apt-get update
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'
sudo apt-get update
apt-cache policy docker-engine
sudo apt-get install -y docker-engine
sudo usermod -aG docker $(whoami)
```
Note: For Windows 7 Pro - Mac OS X use Docker Toolbox.

## Build container
```sh
sudo docker build -t django-docker:latest .
sudo docker run -d --name=<my-container-name> --restart=unless-stopped -e APP_NAME=<app-name> -v <path-on-host>:/srv -p <port-on-host>:8000 django-docker:latest
```
Note: The project folder on container (/srv/<app-name>) shared with host on specified path.

## Usage
Connect to container and manage gunicorn service.
```sh
sudo docker exec -it <my-container-name> /bin/bash
supervisorctl status/stop/start/restart app
```