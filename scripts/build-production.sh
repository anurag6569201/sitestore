#!/bin/bash

# Production build script
# This script builds the React app and prepares Django for production

echo "Building for production..."

# Build React frontend
echo "Step 1: Building React frontend..."
cd frontend
npm run build

if [ $? -ne 0 ]; then
    echo "Error: React build failed!"
    exit 1
fi

echo "React build completed successfully!"

# Return to root
cd ..

# Setup Django for production
echo "Step 2: Setting up Django for production..."
cd backend

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "Production build complete!"
echo ""
echo "To run in production mode:"
echo "1. Update backend/.env with DEBUG=False"
echo "2. Run: cd backend && python manage.py runserver"
echo "   Or use: gunicorn config.wsgi:application"

