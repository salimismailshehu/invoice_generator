# Use a stable Python base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    xfonts-75dpi \
    xfonts-base \
    libxrender1 \
    libxext6 \
    libjpeg62-turbo \
    libpng-dev \
    libfreetype6 \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

# Install wkhtmltopdf manually (compatible version for Debian)
RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.buster_amd64.deb \
    && apt-get update && apt-get install -y ./wkhtmltox_0.12.6-1.buster_amd64.deb \
    && rm wkhtmltox_0.12.6-1.buster_amd64.deb

# Set workdir
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 10000

# Run gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:10000", "app:app"]
