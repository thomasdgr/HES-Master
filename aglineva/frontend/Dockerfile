# DOCKERFILE TO LAUNCH THE MICRO-SERVICE

# Use an official Python runtime as a parent image
FROM nikolaik/python-nodejs:python3.9-nodejs16-alpine

# Set the working directory to /app
WORKDIR /app
RUN mkdir -p /app/api_rest

COPY api_rest/showcase /app/api_rest/showcase
#COPY api_rest/showcase/agilneva-fe/dist /app/api_rest/showcase

WORKDIR api_rest/showcase/agilneva-fe
RUN npm install
RUN npm run build

# Make port 8000 available to the world outside this container
EXPOSE 5173

WORKDIR /app/api_rest/showcase/agilneva-fe

CMD ["python3", "-m", "http.server", "5173" , "--directory" , "dist"]


