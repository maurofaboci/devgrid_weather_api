# Weather Service

## Description

This service collects weather data from the Open Weather API and stores it as JSON data.

## Setup

### Prerequisites
- Docker
- Docker Compose
- python

### Installation

1. **Clone the Repository:**
   This command downloads the project from your remote repository to your local machine.

   git clone https://github.com/maurofaboci/devgrid_weather_api

2. **Navigate to the Project Directory:**
   Changes your working directory to the project folder.

   cd devgrid_weather_service.

3. **Build the Docker Image:**
   Creates a Docker image with the tag `devgrid_weather_service` using the Dockerfile in your project.

   docker build -t devgrid_weather_service .

4. **Run the Docker Container:**
   Starts a container from the image and maps port `8000` of the container to port `8000` on your local machine.

   docker run -d -p 8000:8000 devgrid_weather_service:latest

5. **Verify the Container is Running:**
   Lists the running Docker containers so you can obtain the container ID.

   docker ps

6. **Access the Container and Run Tests:**
   Opens a terminal session inside the running container, allowing you to execute commands such as running tests.

   docker exec -it <your_container_id> /bin/bash

Feel free to adjust any specific details according to your setup or preferences!

OR

**API Documentation**

You can also test the API using the interactive documentation available at /docs on http://localhost:8000/docs after step 4.

OR 

**CURL in terminal**

You can direct curl in the terminal after step 6 

curl -X POST "http://localhost:8000/devgrid/weather" -H "Content-Type: application/json" -d '{"user_id": "<YOUR_UNIQUE_USER_ID>","city_ids": [3439525, 3439781, 3440645, 3442098]}'

curl -X 'GET' 'http://localhost:8000/devgrid/weather/<YOUR_UNIQUE_USER_ID>' -H 'accept: application/json'


curl -X 'GET' 'http://localhost:8000/devgrid/weather_post_info/<YOUR_UNIQUE_USER_ID>' -H 'accept: application/json'