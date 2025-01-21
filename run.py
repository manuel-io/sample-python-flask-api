from app import create_app
import webbrowser
import threading
from dotenv import load_dotenv
import os
from urllib.parse import urlparse

# Load environment variables from .env file
load_dotenv()

app = create_app()

def open_browser():
    api_url = os.getenv('API_URL', 'http://127.0.0.1:5000/api/swagger')
    webbrowser.open_new(api_url + "/swagger")

if __name__ == "__main__":
    if app.config['ENV'] == 'development':
        # Start a thread to open the browser after a short delay
        threading.Timer(1.25, open_browser).start()
    
    # Extract host and port from API_URL
    api_url = os.getenv('API_URL', 'http://127.0.0.1:5000/api')
    parsed_url = urlparse(api_url)
    host = parsed_url.hostname or '127.0.0.1'
    port = parsed_url.port or 5000

    app.run(debug=(app.config['ENV'] == 'development'), host=host, port=port)