# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app

# Expose the port the app runs on
EXPOSE 5000

# Use gunicorn as the production server
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
