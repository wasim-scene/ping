import requests
import time
import threading
from flask import Flask
import threading

app = Flask(__name__)


url = "https://storm-meowing-card.glitch.me/"
@app.route('/')
def index():
    return "Your Flask server is running!"

def run_script():
    while True:
        try:
            response = requests.get(url)
            print(f"Pinged {url} with status code {response.status_code}")
        except Exception as e:
            print(f"Failed to ping {url}: {e}")
        time.sleep(300)
        pass

if __name__ == "__main__":
    # Run the long-running script in a separate thread
    threading.Thread(target=run_script).start()
    app.run(host='0.0.0.0', port=8080)

