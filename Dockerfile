# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /llm-101

# Copy the requirements file into the container at /app/requirements.txt
COPY requirements.txt /llm-101/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . /llm-101/

# Expose the port that the application listens on
EXPOSE 8000

# Run the application
CMD ["uvicorn", "llm:app", "--host", "0.0.0.0", "--port", "8000"]