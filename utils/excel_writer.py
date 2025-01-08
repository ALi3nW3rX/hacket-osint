import os
import pandas as pd
from openpyxl import Workbook, load_workbook
from utils.color_logger import log_info, log_success, log_error, log_warning

def write_to_excel(df, filename="osint_report.xlsx", sheet_name="Sheet1"):
    try:
        # Check if the file exists and create it if not
        if not os.path.exists(filename):
            workbook = Workbook()
            workbook.save(filename)

        # Load the existing workbook
        with pd.ExcelWriter(filename, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            df.to_excel(writer, index=False, sheet_name=sheet_name)

        log_success(f"Data written to {filename} successfully.")
    except Exception as e:
        log_error(f"Error writing to Excel: {str(e)}")
