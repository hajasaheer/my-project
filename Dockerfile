# Use the official Python image as the base
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the application's requirements and source code into the container
COPY requirements.txt requirements.txt
COPY . .

# Install required Python packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the Flask application's default port
EXPOSE 5000

# Define the command to run the application
CMD ["python3", "app.py"]
