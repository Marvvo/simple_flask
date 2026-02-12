# simple_flask
This is a simple Flask API

## Installation
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python app.py`

The API will be available at http://127.0.0.1:5000/

## Docker Deployment
To run the app in a Docker container:

1. Build the Docker image: `docker build -t simple-flask .`
2. Run the container: `docker run -p 5123:5000 simple-flask`

Or use Docker Compose:
1. `docker-compose up --build`

The API will be available at http://localhost:5123/
