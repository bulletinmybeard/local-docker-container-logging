from flask import Flask
import logging
import sys

app = Flask(__name__)

# Setup logger
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def start():
    app.logger.info("Hi 🫡")
    return "Hi 🫡"

@app.route('/hello')
def hello():
    app.logger.info("Hello endpoint was hit")
    return "Hello, World!"

@app.route('/world')
def world():
    app.logger.info("World endpoint was hit")
    return "World, Hello!"

if __name__ == '__main__':
    # Retrieve the app name and server port from the command line arguments
    app_name = sys.argv[1]
    server_port = int(sys.argv[2])

    # Log the message including the app name and server port
    app.logger.info(f"{app_name} demo server starts on port {server_port}")

    # Use the parsed port number in app.run()
    app.run(debug=True, host='0.0.0.0', port=server_port)
