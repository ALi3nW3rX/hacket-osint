import requests
from utils.color_logger import log_success, log_error

def run_chaos(domain, api_key):
    url = f"https://chaos.projectdiscovery.io/api/v1/{domain}/subdomains"
    headers = {"Authorization": api_key}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json().get("subdomains", [])
            log_success(f"Found {len(data)} subdomains for {domain}")
            return data
        else:
            log_error(f"Error: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        log_error(f"Exception occurred: {str(e)}")
        return []

if __name__ == "__main__":
    api_key = "YOUR_API_KEY_HERE"
    domain = "example.com"
    run_chaos(domain, api_key)
