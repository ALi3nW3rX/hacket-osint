import requests

def run_credmaster():
    print("Finding Emails...")
    # Perform OSINT tasks here
    response = requests.get("https://api.hackertarget.com/geoip/?q=example.com")
    print(response.text)

if __name__ == "__main__":
    run_credmaster()
