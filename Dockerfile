# 1. Base Image: Use a lightweight Python image
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file into the container
# We do this first to leverage Docker's layer caching
COPY requirements.txt .

# 4. Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code, models and templates
COPY app.py .
COPY credit_risk_model.pkl .
COPY scaler.pkl .
COPY templates/ ./templates/

# 6. Expose the port that Flask runs on
EXPOSE 5000

# 7. Define the command to run the Flask app
CMD ["python", "app.py"]
