import requests
from utils.color_logger import log_success, log_error

def run_shodan(ip, api_key):
    url = f"https://api.shodan.io/shodan/host/{ip}?key={api_key}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            log_success(f"Shodan Info for {ip}: {data}")
            return data
        else:
            log_error(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        log_error(f"Exception occurred: {str(e)}")
        return None

if __name__ == "__main__":
    api_key = "YOUR_API_KEY_HERE"
    ip = "8.8.8.8"
    run_shodan(ip, api_key)
