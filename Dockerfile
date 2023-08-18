
# create docker file to build image for this flask app
# use python 3.7 as base image

# Update the base image to python 3.8
FROM python:3.8

# set working directory
WORKDIR /app

# add app directory to docker image
ADD . /app

# Update pip to the latest version
RUN pip install --upgrade pip

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# command on container start
# Expose port 500
EX0POSE 5000

# Provide the command to start the flask app
CMD [ "python", "wsgi.py" ]

# Fixed ERROR: Ignored the following versions that require a different python version
# Updated the base image to python:3.8 to match the required python version

# Fixed ERROR: Could not find a version that satisfies the requirement dnspython==2.4.1
# Updated pip install command to include --no-cache-dir option
# This option prevents pip from using the cache when installing dependencies
# It fixed the issue of not being able to find the required version of dnspython