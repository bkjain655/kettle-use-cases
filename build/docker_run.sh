# Run Streamlit Video Coloring Application with GFPGAN and OpenCV
# Requires: app.py, requirements.txt, Dockerfile, streamlit_script.py, gfpgan_model.pth

cd build/
docker-compose up --build -d

docker exec -it <container_name> bash

cd /app
python3 app.py & # Run the application in background for continuous execution