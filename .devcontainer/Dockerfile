# Use a base image with Python
FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Install additional tools or libraries if needed
RUN apt-get update && apt-get install -y \
    git \
    build-essential

# Set the working directory
WORKDIR /workspace

# Copy the current files into the container's working directory
COPY . /workspace

# Default command to run when the container starts
CMD ["bash"]
