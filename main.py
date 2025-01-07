import argparse
import yaml
from tools.crosslinked.crosslinked_tool import run_crosslinked
from tools.subfinder.subfinder_tool import run_subfinder
from online_tools.shodan import run_shodan
from online_tools.chaos import run_chaos
from utils.color_logger import log_info, log_warning, log_error

def load_config():
    with open("configs/config.yaml", "r") as file:
        return yaml.safe_load(file)

   
def main():
    parser = argparse.ArgumentParser(description="Hacket OSINT Automation Script")
    parser.add_argument("-d", "--domain", help="Domain to target")
    parser.add_argument("-e", "--email", help="Email format, e.g., {f}.{last}@domain.com")
    parser.add_argument("-c", "--company", help="Company name")
    parser.add_argument("--tool", help="Specify a single tool to run")
    args = parser.parse_args()

    if args.tool == "crosslinked":
        if args.email and args.company:
            run_crosslinked(args.email, args.company)
        else:
            log_error("You must provide both --email and --company for CrossLinked.")
    elif args.tool == "subfinder":
        if args.domain:
            run_subfinder(args.domain)
        else:
            log_error("You must provide --domain for Subfinder.")
    elif args.tool == "shodan":
        shodan_data = run_shodan("YOUR_API_KEY", "8.8.8.8")
    elif args.tool == "chaos":
        chaos_data = run_chaos("YOUR_API_KEY", "example.com")
    else:
        log_warning("No valid tool specified.")

    log_info("All tasks completed successfully!")

if __name__ == "__main__":
    main()
