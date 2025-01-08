import argparse
import yaml
import subprocess
from tools.crosslinked.crosslinked_tool import run_crosslinked
from tools.subfinder.subfinder_tool import run_subfinder
from tools.checkmdi.check_mdi import get_domains
from online_tools.shodan import run_shodan
from online_tools.chaos import run_chaos
from utils.color_logger import log_info, log_warning, log_error, log_success
from utils.thread_runner import run_in_threads

def load_config():
    with open("configs/config.yaml", "r") as file:
        return yaml.safe_load(file)
    
def run_checkmdi(domain):
    log_info(f"Running CheckMDI for {domain}...")
    try:
        result = subprocess.run(
            ["docker", "exec", "hacket-osint-checkmdi-1", "python3", "/app/check_mdi.py", domain],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if result.returncode == 0:
            log_success("CheckMDI completed successfully!")
        else:
            log_error(f"CheckMDI error: {result.stderr}")
    except Exception as e:
        log_error(f"Error running CheckMDI: {str(e)}")

def run_osint(domain, email_format, company):
    log_info("Running OSINT tools...")

    # Run OSINT Tools Only
    tools_with_args = [
        (get_domains, (domain,)),
        (run_crosslinked, (email_format, company)),
        (run_subfinder, (domain,))
    ]
    
    run_in_threads(tools_with_args)
    log_success("All OSINT tools completed successfully!")
      
def main():
    parser = argparse.ArgumentParser(description="Hacket OSINT Automation Script")
    parser.add_argument("-d", "--domain", help="Domain to target")
    parser.add_argument("-e", "--email", help="Email format, e.g., {f}.{last}@domain.com")
    parser.add_argument("-c", "--company", help="Company name")
    parser.add_argument("--tool", help="Specify a single tool to run")
    parser.add_argument("--osint", action="store_true", help="Run the OSINT Methodology")
    args = parser.parse_args()

    if args.osint:
        if args.domain and args.email and args.company:
            run_osint(args.domain, args.email, args.company)
        else:
            log_error("You must provide --domain, --email, and --company for --osint.")
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
    elif args.tool == "checkmdi":
        if args.domain:
            get_domains(args.domain)
        else:
            log_error("You must provide --domain for CheckMDI.")
    elif args.tool == "shodan":
        shodan_data = run_shodan("YOUR_API_KEY", "8.8.8.8")
    elif args.tool == "chaos":
        chaos_data = run_chaos("YOUR_API_KEY", "example.com")


    log_info("All tasks completed successfully!")

if __name__ == "__main__":
    main()

