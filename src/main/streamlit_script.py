import streamlit as st
import cv2
from PIL import Image
import numpy as np
import os

# Load GFPGAN model and OpenCV dlib face detector
gfpgan_model = 'gfpgan_model.pth'  # Replace with the actual path to your gfpgan_model.pth file
detector = cv2.dnn.readNetFromCaffe(os.path.join('models', 'deploy.prototxt'), os.path.join('models', 'res10_300x300_ssld_iter_140000.caffemodel'))
gfpgan = cv2.dnn.readNetFromTensorflow(gfpgan_model)

# Function to load and process grayscale video frames
def colorize_video():
    cap = cv2.VideoCapture('input_grayscale_video.mp4')  # Replace with the actual path to your input grayscale video file
    out = cv2.VideoWriter('output_colored_video.mp4', cv2.VideoWriter_fourcc(*'MP4V'), cap.get(cv2.CAP_PROP_FPS), (cap.get(3), int(cap.get(4))))  # Replace with the actual desired output video file name and resolution
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert grayscale image to RGB using GFPGAN model
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        gfpgan_output = gfpgan.forward(np.expand_dims([rgb_frame], 0))[0]
        
        # Apply colorization using OpenCV dlib face detector and GFPGAN output
        faces = detector.detect(gfpgan_output, 1)[:5]
        for f in faces:
            x1, y1, w, h = int(f.bbox[0]), int(f.bbx[1]), int(w), int(h)
            
            # Crop and resize the face region to match GFPGAN input size
            cropped_face = gfpgan_output[y1:y1+h, x1:x1+w]
            cropped_face = cv2.resize(cropped_face, (64, 64))
            
            # Apply colorization to the face region using GFPGAN output and OpenCV dlib face detector
            colored_face = gfpgan[0].forward([np.expand_dims(cropped_face, 0)])[0] * 255
            colored_frame = cv2.cvtColor(colored_face, cv2.COLOR_RGB2BGR)
            
        # Combine the colorized face region with the original grayscale image and write to output video file
        frame[:, :w] = colored_frame[:h, :w]
        
        out.write(cv2.merge([rgb_frame[..., 0], rgb_frame[..., 1], colored_frame]))
    cap.release()
    out.release()
    
# Main application code
if __name__ == '__main__':
    st.title('GFPGAN and OpenCV Video Coloring App')
    
    # Load input grayscale video file path from sidebar
    input_video = st.sidebar.file_uploader(label='Upload Grayscale Video', type=['mp4'])
    
    if input_video is not None:
        with open('input_grayscale_video.mp4', 'wb') as f:
            f.write(input_video.read())
            
        
        # Call colorize_video function to process the grayscale video and show a preview in main streamlit window
        st.text('Processing... Please wait until the colored video is ready for playback')
        colorized_video = 'output_colored_video.mp4'  # Replace with the actual desired output video file name
        
        if os.path.exists(colorized_video):
            st.image('preview', use_column_width=True)
            
    else:
        st.text('No grayscale video uploaded')
    
# Dockerfile, requirements.txt and docker_run.sh are not provided in the context so they cannot be included here.