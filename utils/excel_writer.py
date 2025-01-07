import pandas as pd

def generate_excel(data_dict):
    with pd.ExcelWriter("osint_report.xlsx") as writer:
        for tool_name, data in data_dict.items():
            df = pd.DataFrame(data)
            df.to_excel(writer, sheet_name=f"{tool_name} Results", index=False)

if __name__ == "__main__":
    # Example usage
    sample_data = {
        "Chaos": [{"Domain": "example.com", "Subdomain": "sub.example.com"}],
        "Shodan": [{"IP": "8.8.8.8", "Open Ports": [80, 443]}],
        "Subfinder": [{"Subdomain": "sub.example.com"}, {"Subdomain": "test.example.com"}]
    }
    generate_excel(sample_data)
