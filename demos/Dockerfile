# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Docker build arguments
ARG APP_NAME=""
ARG APP_SERVER_PORT=""

# Set environment variables
ENV APP_NAME=$APP_NAME
ENV APP_SERVER_PORT=$APP_SERVER_PORT

# Check if the APP_NAME is empty and exit if it is
RUN if [ -z "$APP_NAME" ]; then echo "APP_NAME argument is required" && exit 1; fi

# Check if the APP_SERVER_PORT is empty and exit if it is
RUN if [ -z "$APP_SERVER_PORT" ]; then echo "APP_SERVER_PORT argument is required" && exit 1; fi

# Set the working directory in the container
WORKDIR /usr/src/app

# Install Flask
RUN pip install Flask

# Copy the current directory contents into the container at /usr/src/app
COPY ./app.py .

# Make port 5000 available to the world outside this container
EXPOSE $APP_SERVER_PORT

# Run app.py when the container launches
CMD python ./app.py $APP_NAME $APP_SERVER_PORT
