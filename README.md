# Weather Service

## Description

This service collects weather data from the Open Weather API and stores it as JSON data.

## Setup

### Prerequisites
- Docker
- Docker Compose

### Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd devgrid_weather_service.

   docker build -t devgrid_weather_service .
   docker run -d -p 8000:8000 devgrid_weather_service:latest