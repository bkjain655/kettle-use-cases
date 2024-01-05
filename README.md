 Title: Streamlit Video Coloring App with GFPGAN and OpenCV

This repository contains a streamlit application that utilizes the power of deep learning to colorize grayscale videos. The app leverages GFPGAN, an AI model for generating realistic images from unpaired data, along with OpenCV for video processing. It's designed as a Dockerized solution for easy deployment and portability across different environments.

Features:
1. Browse and load grayscale videos using the sidebar.
2. Apply colorization to input videos through GFPGAN model (gfpgan_model.pth).
3. Display colored video frames in real-time within the main streamlit window, showing every 30th frame for performance optimization.
4. Dockerized application with a custom script `docker_run.sh` to simplify deployment and management.
5. Modular structure that allows easy maintenance of codebase and dependencies (requirements.txt).
6. Separate directory for OpenCV modules, libs/opencv_modules.
7. Build artifacts are stored in the `build` directory.

Getting Started:
1. Clone this repository to your local machine using git clone https://github.com/your-username/streamlit-video-coloring-app.git
2. Navigate into the project folder and run `docker build -t streamlit_videocolor .` from within it. This will create a Docker image containing all necessary dependencies for your application.
3. Run `docker run --rm -it -p 8501:8501 streamlit_videocolor` to start the container and launch the app on port 8501 in your browser at http://localhost:8501/.
4. Browse for a grayscale video file, select it from the sidebar, and click "Process" to colorize the input video. The colored frames will be displayed within the main streamlit window.

Contributing:
We welcome contributions! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix (`git checkout -b my-new-feature`)
3. Commit and push changes to your fork.
4. Submit a pull request with a clear description of your contribution, including any necessary contextual information.
5. Our team will review the code and merge it if approved.

---

# Create A Streamlit Video Coloring Application Using Gfpgan And Opencv. The Application Should Browse For A Grayscale Video, Process, And Emit A Colored Video File. The Application Should Also Have A Sidebar To Browse For The Input Grascale Videe. It Must Use Main Streamlit Window To Show A Preview Of The Colored Video (Every 30Th Colored Frame). Use Docker To Ship This Application.
This artifact is created by [Kettle](kettle.gnyan.ai) Promptware Development Hub.
- Date: `2024-01-02 13:56:30`
- Model: `neural-chat:latest`
- File Prompt: <pre>You are an EXPERT developer who will design, structure, and write great software application code.<br>Given a brief description of a story, you will first create a file structure of the necessary files and folders.<br>For example, a python hello world program will require main.py, requirements.txt, Dockerfile, readme.md, docker\_run.sh files: your response will therefore be --<br>\`\`\`files<br>\[\("main.py", "", "file"\), <br>\("requirements.txt", "", "file"\), <br>\("docs", "", "dir"\), <br>\("readme.md", "docs", "file"\), <br>\("Dockerfile", "", "file"\), <br>\("build", "", "dir"\), <br>\("docker\_build.sh", "build", "file"\), <br>\("docker\_run.sh", "build", "file"\)\]<br>\`\`\`<br>Take a deep breath and reason step-by-step. Please be exhaustive in the files you create. <br>You will NOT need \`requirements.txt\` for non Python application, in such instances, feel free to deviate from requirements archetype. Choose appropriate dependency file for the programming language: for example, in Perl, you will create cpanfile instead of requirements.txt.<br>You will present a single manifest of files: You are NOT allowed to split subfolder listings in your response.<br>For example, \`\`\`<br>Inside the 'build/src' directory: \[\("main.py", "", "file"\), \("utils.py", "", "file"\), \(".gitignore", "", "file"\)\]\`\`\` is prohibited.<br>\`\`\`files \[\("build", "", "dir"\), \("src", "build", "dir"\), \("main.py", "build/src", "file"\), \("utils.py", "build/src", "file"\), \(".gitignore", "build/src", "file"\)\]\`\`\` is allowed.<br>Each tuple in the response will be a triple of \(filename, directory path, type\). Filename MUST be a filename ONLY, not a path. directory path MUST be a path ONLY, not a filename.<br><br>You are NOT allowed to offer multiple options like sbt or gradlew or maven archetypes. Choose ONE best option.<br>You want to be very diligent in the directory structure. Your response MUST be in the form of a single list of tuples. Each tuple is a \(file|directory name, its base directory path, and its type \{\{\{\{file|dir\}\}\}\}\). <br>Make the directory path relative to the top level directory. You ARE NOT ALLOWED to create directories outside of the top level directory.<br>ALWAYS quote filenames and directories that have whitespaces. Surround the response in \`\`\` backticks at the start and end<br>Description: '''\{\{question\}\}'''<br>Response: <br>\`\`\`files<br></pre>
- README Prompt: <pre>You are an EXPERT developer who will design, structure, and write great software application code. <br>Given a brief description of a story and a file layout, you will author a readme.md file. <br>You will respond with the contents of the readme.md file ONLY. Respond in markdown format and surround the response in \`\`\` backticks at the start and end. Please be VERY brief and ONLY respond in markdown format to the question.<br>Deliberate the desscription and add some interpreted markdown to the readme.md file.<br>Description: '''\{\{question\}\}'''<br>File Layout: '''\{\{file\_layout\}\}'''<br>\`\`\`readme.md<br></pre>
- Artifact: `artifacts/F026CEAA90D5E93B64D9AF6226A56124`
---
