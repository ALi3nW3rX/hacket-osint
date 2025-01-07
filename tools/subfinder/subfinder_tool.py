import subprocess
import os
import pandas as pd
from utils.color_logger import log_info, log_success, log_error
from utils.excel_writer import write_to_excel

def run_subfinder(domain):
    log_info(f"Running Subfinder for {domain}...")

    try:
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

            # Filter out unnecessary lines and capture only subdomains
            subdomains = [
                line for line in result.stdout.splitlines()
                if not line.startswith("Subfinder config generated successfully!")
            ]

            if subdomains:
                df = pd.DataFrame(subdomains, columns=["Subdomains"])
                write_to_excel(df, sheet_name="Subfinder")
            else:
                log_warning("No subdomains found.")
        else:
            log_error(f"Subfinder error: {result.stderr}")
    except Exception as e:
        log_error(f"Exception occurred while running Subfinder: {str(e)}")
