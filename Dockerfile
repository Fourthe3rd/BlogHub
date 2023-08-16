
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
# Expose port 5000
EXPOSE 5000

# Provide the command to start the flask app
CMD [ "python", "run.py" ]

# Fixed ERROR: Ignored the following versions that different
# Fixed ERROR: Could not find version that satisfies the requirement dnspython==2.4.1
# Updated pip install command to include --no-cache-dir option
# This option prevents pip from using the cache when installing dependencies
# Changed the base image to python:3.8 as the error message suggests that the image build failedundefined
