
# create docker file to build image for this flask app
# use python 3.7 as base image
FROM python:3.7
# set working directory
WORKDIR /app
# add app directory to docker image
ADD . /app
# update pip
RUN pip install --upgrade pip

# install dependencies
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python", "run.py" ]

# Expose port 5000
EXPOSE 5000 
