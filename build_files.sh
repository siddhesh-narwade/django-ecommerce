#!/bin/bash

# Install dependencies (use --break-system-packages for Vercel's uv-managed Python)
pip install -r requirements.txt --break-system-packages

# Run migrations
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Seed the database with sample products
python seed_db.py
python create_admin.py

# Collect static files
python manage.py collectstatic --noinput
