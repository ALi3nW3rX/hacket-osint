import os
import pandas as pd
import argparse
import subprocess
import yaml
import requests
from utils.color_logger import log_info, log_success, log_warning, log_error
from utils.excel_writer import write_to_excel
from online_tools.shodan import run_shodan
from online_tools.chaos import run_chaos
from utils.excel_writer import write_to_excel

def load_config():
    with open("configs/config.yaml", "r") as file:
        return yaml.safe_load(file)

# Function to run Shodan
def run_shodan(api_key, ip):
    log_info(f"Running Shodan lookup for {ip}...")
    try:
        url = f"https://api.shodan.io/shodan/host/{ip}?key={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            log_success("Shodan lookup successful!")
            return response.json()
        else:
            log_error(f"Shodan API error: {response.status_code}")
            return {}
    except Exception as e:
        log_error(f"Error running Shodan: {str(e)}")
        return {}

# Function to run Chaos
def run_chaos(api_key, domain):
    log_info(f"Running Chaos lookup for {domain}...")
    try:
        url = f"https://chaos.projectdiscovery.io/api/v1/{domain}/subdomains"
        headers = {"Authorization": api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            log_success("Chaos lookup successful!")
            return response.json()
        else:
            log_error(f"Chaos API error: {response.status_code}")
            return {}
    except Exception as e:
        log_error(f"Error running Chaos: {str(e)}")
        return {}
    
# Function to run CrossLinked
def run_crosslinked(email_structure, company_name):
    log_info(f"Running CrossLinked for {company_name} with email structure {email_structure}...")

    try:
        # Run CrossLinked inside the Docker container
        result = subprocess.run(
            [
                "docker",
                "run",
                "--rm",
                "-v",
                f"{os.getcwd()}/output:/app/output",
                "hacket-osint-crosslinked",
                "-f",
                email_structure,
                company_name
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            log_success("CrossLinked completed successfully!")

            # Check for names.csv and names.txt
            csv_file = "output/names.csv"
            txt_file = "output/names.txt"

        # Write names.csv to the Employees tab
        if os.path.exists("output/names.csv"):
            df_employees = pd.read_csv("output/names.csv")
            write_to_excel(df_employees, sheet_name="Employees")

        # Write names.txt to the Emails tab
        if os.path.exists("output/names.txt"):
            with open("output/names.txt", "r") as f:
                emails = [line.strip() for line in f.readlines()]
            df_emails = pd.DataFrame(emails, columns=["Emails"])
            write_to_excel(df_emails, sheet_name="Emails")

        else:
            log_error(f"CrossLinked error: {result.stderr}")
    except Exception as e:
        log_error(f"Exception occurred while running CrossLinked: {str(e)}")

# Main function
def main():
    parser = argparse.ArgumentParser(description="Hacket OSINT Automation Script")
    parser.add_argument("-d", "--domain", help="Domain to target")
    parser.add_argument("-e", "--email", help="Email format, e.g., {f}.{last}@domain.com")
    parser.add_argument("-c", "--company", help="Company name")
    parser.add_argument("--tool", help="Specify a single tool to run")
    args = parser.parse_args()

    if args.tool == "crosslinked":
        if args.email and args.company:
            output = run_crosslinked(args.email, args.company)
            write_to_excel({"CrossLinked": output})
        else:
            log_error("You must provide both --email and --company for CrossLinked.")
    else:
        log_warning("No valid tool specified.")
        
    config = load_config()
    shodan_api_key = config["shodan"]["api_key"]
    chaos_api_key = config["chaos"]["api_key"]

    # Example: Run Shodan and Chaos
    shodan_data = run_shodan(shodan_api_key, "8.8.8.8")
    chaos_data = run_chaos(chaos_api_key, "example.com")

    log_success("All tasks completed successfully!")        
    

if __name__ == "__main__":
    main()
