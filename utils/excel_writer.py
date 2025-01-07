import pandas as pd
from openpyxl import load_workbook

def write_to_excel(df, sheet_name="Sheet1"):
    filename = "osint_report.xlsx"
    
    try:
        # Check if the file exists, load it; otherwise, create a new Excel file
        try:
            writer = pd.ExcelWriter(filename, mode='a', engine='openpyxl')
        except FileNotFoundError:
            writer = pd.ExcelWriter(filename, mode='w', engine='openpyxl')

        # Write the DataFrame to the specified sheet
        df.to_excel(writer, index=False, sheet_name=sheet_name)

        # Save the workbook
        writer.close()

        print(f"Data written to {filename} successfully.")
    except Exception as e:
        print(f"Error writing to Excel: {str(e)}")
