# Use the official Python image as the base
FROM python:3.11-slim

# Install locust
RUN pip install locust

# Set the working directory in the container
WORKDIR /locust

# Copy the Locustfile to the working directory
COPY locustfile.py .

# Expose Locust port (default 8089)
EXPOSE 8089

# Command to run Locust in headless mode (remove --headless to use the UI)
CMD ["locust", "-f", "multipleTaskWithWeight.py", "--host=http://your-target-host", "--web-host=0.0.0.0"]
