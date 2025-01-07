# Hacket OSINT

[toc]

## Overview
Hacket OSINT is a fully dockerized, modular OSINT (Open-Source Intelligence) tool designed for cybersecurity professionals and penetration testers. The tool allows users to run multiple OSINT tools as microservices via Docker containers. The output from each tool is collected and consolidated into a single Excel report with multiple tabs, providing a comprehensive view of the gathered data.

---

## Features
- **Modular Microservices**: Each OSINT tool runs as its own Docker container to avoid dependency issues.
- **Integrated Tools**:
  - Subfinder (Subdomain Enumeration)
  - CrossLinked (LinkedIn Enumeration)
  - Shodan (Internet-wide Scanning)
  - Chaos (Project Discovery)
- **Dynamic Configurations**: API keys and tool configurations are managed through a central YAML config file.
- **Command-line Interface**: Users can run the tool via CLI with single-line arguments or through an interactive wizard.
- **Excel Report Generation**: Consolidated results from all tools are saved into a multi-tab Excel report.

---

## Prerequisites
- Docker
- Docker Compose
- Python 3.10+

---

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/hacket-osint.git
   cd hacket-osint
   ```

2. **Build the Docker images:**
   ```bash
   docker-compose build
   ```

3. **Start the Docker containers:**
   ```bash
   docker-compose up -d
   ```

---

## Usage
You can run Hacket OSINT through the command line.

### Example Commands
- **Run all tools with arguments:**
  ```bash
  python3 main.py -d domain.com -e "{f}.{last}@domain.com" -c "Example Corp"
  ```
- **Run a specific tool:**
  ```bash
  python3 main.py -d domain.com --tool subfinder
  ```

---

## Configuration
All API keys and settings are managed through the **`configs/config.yaml`** file.

### Example `config.yaml`
```yaml
chaos:
  api_key: "your_chaos_api_key"

shodan:
  api_key: "your_shodan_api_key"

subfinder:
  providers:
    - "virustotal"
    - "securitytrails"
  api_keys:
    virustotal: "your_virustotal_api_key"
    securitytrails: "your_securitytrails_api_key"
    chaos: "your_chaos_api_key"
```

---

## Tools
### CrossLinked
CrossLinked is a LinkedIn enumeration tool designed to gather employee data from LinkedIn.

**Command:**
```bash
python3 main.py -e "{f}.{last}@domain.com" -c "Example Corp" --tool crosslinked
```

### Subfinder
Subfinder is a fast subdomain enumeration tool that discovers valid subdomains for websites using passive sources.

**Command:**
```bash
python3 main.py -d domain.com --tool subfinder
```

---

## Output
The output of each tool is consolidated into an Excel file named **`osint_report.xlsx`**. Each tool's results are written to a separate tab within the Excel file.

### Example Tabs:
- **CrossLinked**: Employee emails and LinkedIn data.
- **Subfinder**: Subdomains discovered.
- **Shodan**: Shodan scan results.
- **Chaos**: Project Discovery's Chaos results.

---

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

---

## License
This project is licensed under the MIT License. See the **LICENSE** file for more details.

---

## Contact
For any inquiries or issues, contact:

- **GitHub:** [ali3nw3rx](https://github.com/ali3nw3rx)
