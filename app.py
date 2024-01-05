from flask import Flask
app = Flask(__name__)  # Create a Flask app instance with the current file's name as its base name.

@app.route('/')  # Define route for root URL '/'.
def hello_world():  # Function to handle requests on this route.
    return 'Hello, World!'  # Return a string response when requested at this path.

if __name__ == "__main__":  # Run the app if this file is executed directly.
    app.run(debug=True)  # Start Flask server in debug mode for easy development and error handling.