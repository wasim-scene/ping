import requests
import time

url = "https://storm-meowing-card.glitch.me/"

while True:
    try:
        response = requests.get(url)
        print(f"Pinged {url} with status code {response.status_code}")
    except Exception as e:
        print(f"Failed to ping {url}: {e}")
    time.sleep(300)  # Sleep for 5 minutes
