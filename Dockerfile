# Step 1: Use the official Python image from Docker Hub
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the Flask application code into the container
COPY . /app

# Step 5: Expose the port that Flask will run on (default 5000)
EXPOSE 5000

# Step 6: Set environment variables to allow Flask to run on all interfaces
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Step 7: Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
