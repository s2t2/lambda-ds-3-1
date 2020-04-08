
# Notes and Reference Materials - Class 3

Lambda Material:

  + https://learn.lambdaschool.com/ds/module/recLjxZbBV3Jmrj2T/
  + https://github.com/LambdaSchool/DS-Unit-3-Sprint-1-Software-Engineering/tree/master/module3-containers-and-reproducible-builds

## Part I and II

Review of Virtual Environments and OOP

  + [Class 1](class-1.md)
  + [Class 2](class-2.md)

Review of the Lambdata Package Functionality:

  + [Functional Approach](/app/class-2/assignment_func.py)
  + [OOP Approach](/app/class-2/assignment_oop.py)
  + [Inheritance Approach](/app/class-2/assignment_oop_inherit.py)

## Part III

Using a Docker image:

```sh
docker run hello-world
```

Using a Dockerfile:

```sh
# Dockerfile

FROM debian

### So logging/io works reliably w/Docker
ENV PYTHONUNBUFFERED=1
### UTF Python issue for Click package (pipenv dependency)
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
### Need to explicitly set this so `pipenv shell` works
ENV SHELL=/bin/bash

### Basic Python dev dependencies
RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install python3-pip curl -y && \
  pip3 install pipenv

### Install via pip or pipenv:
RUN pip3 install pandas
#RUN pipenv install pandas
```

Run from the directory where the dockerfile is:

```sh
docker build . -t my_python_image # builds a new docker image

docker run -it my_python_image /bin/bash # starts up a new container of a docker image

# mess around with python3, pip3, pipenv inside the container
# then exit

docker container ls --all # find all container names and IDs

docker start <container id> # starts a paused docker container

docker attach <container id> # reconnects to a running docker container
```

> Special [thanks](https://app.slack.com/client/T4JUEB3ME/GPP0JA5RD/thread/GPP0JA5RD-1581534096.091100) to Benjamin and Caleb from DS 11

FYI: Here's a more in-depth walkthrough of Docker, for those who are interested:

  + https://youtu.be/nrzxKL4bsLI
