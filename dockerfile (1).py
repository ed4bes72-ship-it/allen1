# Use an official Python runtime
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of your code
COPY . .

# Run the app using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
