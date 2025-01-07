# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install necessary system packages
RUN apt-get update && apt-get install -y git

# Clone the CrossLinked repository
RUN git clone https://github.com/m8sec/crosslinked.git

# Change into the CrossLinked directory
WORKDIR /app/crosslinked

# Install Python dependencies
RUN pip3 install .

# Copy the entrypoint script
COPY entrypoint.sh /app/crosslinked/entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /app/crosslinked/entrypoint.sh

# Set the entrypoint to run CrossLinked with dynamic arguments
ENTRYPOINT ["./entrypoint.sh"]
