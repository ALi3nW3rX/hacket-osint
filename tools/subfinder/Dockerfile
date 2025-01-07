# Use a lightweight Debian image
FROM debian:bullseye-slim

# Set the working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip

# Download and install the latest Subfinder binary
RUN wget https://github.com/projectdiscovery/subfinder/releases/download/v2.5.8/subfinder_2.5.8_linux_amd64.zip && \
    unzip subfinder_2.5.8_linux_amd64.zip && \
    mv subfinder /usr/local/bin/ && \
    rm subfinder_2.5.8_linux_amd64.zip

# Set the entrypoint to Subfinder
ENTRYPOINT ["subfinder"]
