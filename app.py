from streamlit_script import st
import cv2, os
from gfpgan.gfpgan import GFPGAN

# Load the pre-trained model and set up GPU usage if available
model = GFPGAN(use_gpu=True)  # Replace with actual path to your trained model

def main():
    st.title("Streamlit Video Coloring App")

    # Sidebar for selecting grayscale video file
    sidebar = st.sidebar.file_uploader('Upload Grayscale Video', type=['mp4'])
    if not sidebar:  # If no file is selected, exit the program
        return

    # Load and convert uploaded grayscale video to RGB format for previewing in main window
    gray_video = cv2.VideoCapture(sidebar)
    rgb_video = cv2.cvtColor(gray_video, cv2.COLOR_GRAY2BGR)
    fps = gray_video.get(cv2.CAP_PROP_FPS)  # Get video frame rate

    # Create a folder to save the colored output videos if it doesn't exist already
    colored_videos_folder = 'colored_videos'
    os.makedirs(colored_videos_folder, exist_ok=True)

    # Main window for previewing and processing video frames
    st.write("Preview of Colored Video")
    while True: 
        ret, frame = gray_video.read()
        if not ret: break
        
        colored_frame = model(frame)  # Apply colorization to the grayscale frame using GFPGAN
        st.image(colored_frame)  # Display preview of colored video in main window

    # Save colored frames as a new output video file
    out = cv2.VideoWriter('{}/output_{}.mp4'.format(colored_videos_folder, os.path.basename(sidebar)), cv2.VideoWriter_fourcc(*'MP4V'), fps, (rgb_video.shape[1], rgb_video.shape[0]))
    for i in range(gray_video.get(cv2.CAP_PROP_FRAME_COUNT)):  # Iterate through all video frames
        ret, frame = gray_video.read()
        
        if not ret: break
        colored_frame = model(frame)
        out.write(colored_frame)
    out.release()
    
if __name__ == '__main__':
    main()