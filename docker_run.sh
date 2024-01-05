#!/bin/bash
# Run Streamlit application in Docker container

docker build -t streamlit-app .
docker run --rm \
  -p 8501:8501 \
  -v $(pwd)/geojson_data:/usr/src/app/geojson_data \
  -e STREAMLIT_SERVER_PORT=8501 \
  streamlit-app python main.py