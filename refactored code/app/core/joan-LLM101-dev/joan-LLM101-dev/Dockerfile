# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user and application directory
RUN useradd -r -s /bin/false appuser && \
    mkdir /app && \
    chown appuser:appuser /app

# Set the working directory in the container
WORKDIR /app

# # Copy requirements first for caching
COPY requirements.txt .

# Install Python dependencies securely
RUN pip install --no-cache-dir --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# Copy application code with proper permissions
COPY --chown=appuser:appuser . .

# Security hardening
RUN find /app -type d -exec chmod 755 {} \; && \
    find /app -type f -exec chmod 644 {} \; && \
    chmod 755 /app

# Switch to non-root user
USER appuser

# Expose the port that the application listens on
EXPOSE 8000

# Health check with timeout
HEALTHCHECK --interval=60s --timeout=10s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8991/health || exit 1

# Run the application with production settings
CMD ["python", "main.py"]

