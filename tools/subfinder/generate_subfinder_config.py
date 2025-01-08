import yaml
import os
from utils.color_logger import log_info, log_success, log_error, log_warning

def generate_subfinder_config():
    # Load the main config.yaml
    with open("configs/config.yaml", "r") as file:
        main_config = yaml.safe_load(file)

    # Extract the relevant keys for Subfinder
    subfinder_config = {
        "sources": main_config.get("subfinder", {}).get("providers", ["all"]),
        "keys": {
            "virustotal": main_config.get("subfinder", {}).get("api_keys", {}).get("virustotal", ""),
            "securitytrails": main_config.get("subfinder", {}).get("api_keys", {}).get("securitytrails", ""),
            "chaos": main_config.get("subfinder", {}).get("api_keys", {}).get("chaos", "")
        }
    }

    # Ensure the directory exists
    os.makedirs("/root/.config/subfinder", exist_ok=True)

    # Write the Subfinder config file
    with open("/root/.config/subfinder/config.yaml", "w") as file:
        yaml.dump(subfinder_config, file)

    log_info(f"Subfinder config generated successfully!")

if __name__ == "__main__":
    generate_subfinder_config()
