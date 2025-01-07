# Use the latest Go image with Go 1.21
FROM golang:1.21

# Set the working directory
WORKDIR /app

# Install Subfinder globally
RUN go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# Install Python and necessary packages
RUN apt-get update && apt-get install -y python3 python3-pip && pip3 install --break-system-packages pyyaml

# Copy the entrypoint script and the config generator
COPY ./entrypoint.sh /app/entrypoint.sh
COPY ./generate_subfinder_config.py /app/tools/subfinder/generate_subfinder_config.py

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
