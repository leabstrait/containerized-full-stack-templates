# Use the Python 3.9-slim base image
FROM python:3.9-slim as build-stage

# Set the working directory in the container
WORKDIR /app

# Copy your entire application code to the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your application will run on
# EXPOSE 8080

# Define the command to run your FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
