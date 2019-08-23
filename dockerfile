#Grab the latest alpine image
FROM python:3.7.4

# Install python and pip
COPY ./requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

# Add our code
COPY ./api /opt/api/
WORKDIR /opt/api

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku			
CMD gunicorn --bind 0.0.0.0:$PORT wsgi 
