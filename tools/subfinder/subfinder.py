import subprocess
from utils.color_logger import log_info, log_success, log_error

def run_subfinder(domain):
    log_info(f"Running Subfinder for {domain}...")
    
    try:
        # Run Subfinder inside the Docker container
        result = subprocess.run(
            ["docker", "exec", "subfinder", "subfinder", "-d", domain],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            log_success("Subfinder completed successfully!")
            subdomains = result.stdout.splitlines()
            return subdomains
        else:
            log_error(f"Subfinder error: {result.stderr}")
            return []
    except Exception as e:
        log_error(f"Exception occurred: {str(e)}")
        return []

if __name__ == "__main__":
    domain = "example.com"
    subdomains = run_subfinder(domain)
    print("\n".join(subdomains))
