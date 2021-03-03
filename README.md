# Simple Kubernetes Demo Project

This is a simple Flask app which runs on Kubernetes and will return the latest git commit hash for the provided Repo on a health check url 

# How to run

_Pre requisites:_
Kubernetes installed

Apply the provided Manifests to deploy the Application and start the service using the below commands

_kubectl apply -f https://raw.githubusercontent.com/anbuselvidemo/KUBEDEMO/main/deployment.yaml_

_kubectl apply -f https://raw.githubusercontent.com/anbuselvidemo/KUBEDEMO/main/service.yaml_

_launch  http://localhost/gitversion to access the health check url_

# How to replicate the project 
The project uses docker to build the container image, jenkins to create the image from the source code and then pushes the same to docker hub.

_Pre requisites:_
docker installed 
Jenkins setup
configure a webhook from git to Jenkins
docker hub credentials on Jenkins

- Clone the repo
- Update the required github repo url in app.py
- Update the docker hub repo name in Jenkinsfile
- Update the docker hub credential id in Jenkinsfile
- Update the docker image name in deployment.yaml

Create a multi branch pipeline in Jenkins and configure your github url. 
A push/commit to Github will trigger a build and push the new version of the app to docker hub.

# NOTE
The demo app reads the github hash and shares it. In an actual application, the Githash details and Build Version can be pushed to a changelog/artifactory and that can be used to show the details on the healthcheck url
