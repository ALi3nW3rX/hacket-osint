import subprocess
import os
import yaml
from utils.color_logger import log_info, log_success, log_error, log_warning
from tools.subfinder.generate_subfinder_config import generate_subfinder_config

def run_subfinder(domain):
    log_info(f"Running Subfinder for {domain}...")

    try:
        # Generate the Subfinder config file
        generate_subfinder_config()

        # Run Subfinder as a subprocess
        result = subprocess.run(
            [
                "docker",
                "run",
                "--rm",
                "-v",
                f"{os.getcwd()}/output:/app/output",
                "hacket-osint-subfinder",
                "-d",
                domain
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            log_success("Subfinder completed successfully!")

            # Filter the output to extract subdomains
            subdomains = [
                line.strip() for line in result.stdout.splitlines() if line and not line.startswith("[")
            ]

            if subdomains:
                return subdomains
            else:
                log_warning("No subdomains found.")
                return []
        else:
            log_error(f"Subfinder error: {result.stderr}")
            return []
    except Exception as e:
        log_error(f"Exception occurred while running Subfinder: {str(e)}")
        return []


if __name__ == "__main__":
    generate_subfinder_config()
    domain = "example.com"
    results = run_subfinder(domain)
    if results:
        for subdomain in results:
            print(subdomain)
