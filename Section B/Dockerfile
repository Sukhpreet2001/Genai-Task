FROM python:3.11.3

# Set environment variable
ENV PYTHONUNBUFFERED True

# Create working directory
ENV APP_HOME /app
WORKDIR $APP_HOME

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port 8080
EXPOSE 8080

# Command to run the application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]

