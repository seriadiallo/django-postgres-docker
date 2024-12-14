FROM python:3.10-slim-bullseye
LABEL author="Sadialiou Diallo"
LABEL maintainer="SD"
LABEL version="1.2"

# Set environment variables to prevent pyc files and limit buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    make \
    libpq-dev \
    libffi-dev \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    libopenblas-dev \
    libtiff5-dev \
    bash \
    ffmpeg \
    libsm6 \
    libxext6 \
    build-essential \
    python3-dev \
    sqlite3 \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install dependencies
RUN pip install --upgrade pip setuptools

# Copy the requirements file to the container
COPY ./requirements.txt /tmp/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Create a non-root user
# RUN useradd \
#     --no-create-home \
#     django-user


RUN adduser -u 5678  --no-create-home --disabled-password --gecos "" django-user && chown -R django-user /app/
# Copy application files
COPY --chown=django-user:django-user ./ /app/

# Switch to non-root user
USER django-user