#!/bin/bash

# Setup script for Django backend

echo "Setting up Django backend..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    cp .env.example .env
    echo "Please edit .env file and set your SECRET_KEY"
fi

# Run migrations
echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Setup complete!"
echo "To start the server, run: python manage.py runserver"

