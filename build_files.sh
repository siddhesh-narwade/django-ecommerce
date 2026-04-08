#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Seed the database with sample products
python seed_db.py

# Collect static files
python manage.py collectstatic --noinput
