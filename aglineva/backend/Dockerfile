# DOCKERFILE TO LAUNCH THE MICRO-SERVICE

# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app
RUN mkdir -p /app/api_rest

# Copy the requirements file into the container at /app
COPY api_rest/requirements.txt /app/api_rest/requirements.txt
COPY api_rest/restaurants.json restaurants.json

# Upgrade pip if necessary
RUN pip3 install --upgrade pip
RUN pip3 --version

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r /app/api_rest/requirements.txt

COPY api_rest/*.py /app/api_rest/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "api_rest.main:rootapp"]

