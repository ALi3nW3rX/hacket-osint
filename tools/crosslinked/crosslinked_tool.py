import os
import pandas as pd
import subprocess
from utils.excel_writer import write_to_excel
from utils.color_logger import log_info, log_success, log_error

def run_crosslinked(email_structure, company_name):
    log_info(f"Running CrossLinked for {company_name} with email structure {email_structure}...")

    try:
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
            if os.path.exists("output/names.csv"):
                df_employees = pd.read_csv("output/names.csv")
                write_to_excel(df_employees, sheet_name="Employees")

            if os.path.exists("output/names.txt"):
                with open("output/names.txt", "r") as f:
                    emails = [line.strip() for line in f.readlines()]
                df_emails = pd.DataFrame(emails, columns=["Emails"])
                write_to_excel(df_emails, sheet_name="Emails")

        else:
            log_error(f"CrossLinked error: {result.stderr}")
    except Exception as e:
        log_error(f"Exception occurred while running CrossLinked: {str(e)}")
