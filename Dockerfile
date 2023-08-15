
# create docker file to build image for this flask app
# use python 3.7 as base image
FROM python:3.7

# set working directory
WORKDIR /app

# add app directory to docker image
ADD . /app# update pip
RUN pip install --upgrade pip

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# command on container start
# Expose port 5000
EXPOSE 5000

CMD [ "python", "run.py" ]

# Fixed ERROR: Ignored the following versions that different
# Fixed ERROR: Could not find version that satisfies the requirement dnspython==2.4.1
# Updated pip install command to include --no-cache-dir option
# This option prevents pip from using the cache when installing dependencies
 helps errors caused
