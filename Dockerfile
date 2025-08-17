# Use Ubuntu 20.04 LTS as base (wkhtmltopdf supported here)
FROM ubuntu:20.04

# Prevent interactive prompts during package installs
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies and wkhtmltopdf
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    wkhtmltopdf \
    xfonts-75dpi \
    xfonts-base \
    libxrender1 \
    libxext6 \
    libjpeg62-turbo \
    libpng16-16 \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Copy project files
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY . .

# Expose port (Render expects this)
EXPOSE 5000

# Default run command
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
