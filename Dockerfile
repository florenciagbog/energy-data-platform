# Use an official Python image
FROM python:3.14-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency list into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the ingestion script into the container
COPY src/ ./src/

# Run the EIA ingestion pipeline
CMD ["python", "src/eia_ingestion.py"]