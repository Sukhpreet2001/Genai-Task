FROM python:3.11.3

# Set environment variable
ENV PYTHONUNBUFFERED=True

# Create working directory
ENV APP_HOME=/app
WORKDIR $APP_HOME

# Install dependencies and upgrade SQLite
RUN apt-get update && apt-get install -y wget build-essential libsqlite3-dev \
    && wget https://www.sqlite.org/2023/sqlite-autoconf-3410200.tar.gz \
    && tar -xvzf sqlite-autoconf-3410200.tar.gz \
    && cd sqlite-autoconf-3410200 \
    && ./configure && make && make install \
    && cd .. && rm -rf sqlite-autoconf-3410200* \
    && ldconfig

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port 8080
EXPOSE 8080

# Command to run the application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]
