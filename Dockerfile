# Use an official lightweight Python image
FROM python:3.10-slim

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies for wkhtmltopdf and fonts
RUN apt-get update --fix-missing && apt-get install -y --no-install-recommends \
    wkhtmltopdf \
    fonts-dejavu \
    libxrender1 \
    libxext6 \
    libjpeg62-turbo \
    libpng-dev \
    libfreetype6 \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 5000

# Run the app with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
