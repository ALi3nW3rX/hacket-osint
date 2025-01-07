import argparse
import yaml
from tools.online_tools.chaos.chaos import run_chaos
from tools.online_tools.shodan.shodan import run_shodan
from utils.color_logger import log_info, log_success, log_warning, log_error

def load_config():
    with open("configs/config.yaml", "r") as file:
        return yaml.safe_load(file)

def main():
    parser = argparse.ArgumentParser(description="OSINT Automation Script")
    parser.add_argument("--tool", help="Run a specific tool")
    parser.add_argument("--domain", help="Domain name for OSINT tools")
    parser.add_argument("--ip", help="IP address for Shodan tool")
    args = parser.parse_args()

    config = load_config()

    if args.tool == "chaos" and args.domain:
        run_chaos(args.domain, config["chaos"]["api_key"])
    elif args.tool == "shodan" and args.ip:
        run_shodan(args.ip, config["shodan"]["api_key"])
    else:
        log_warning("Please provide a valid tool and input.")

    log_success("All tasks completed successfully!")

if __name__ == "__main__":
    main()
