#!/bin/bash

# run Django

function manage_app () {
  # Generate and apply new migrations
  python manage.py makemigrations
  python manage.py migrate
}

function start_development() {
  # Run the integrated server for development
  echo "Trying to run development server"
  manage_app
  # For remote debugging, only one thread so, no hot reloading
  python manage.py runserver --noreload --nothreading 0.0.0.0:8000
  echo "Development server running"
}

function start_production() {
  # For production, we use gunicorn
  echo "Trying to run production server"
  manage_app
  python manage.py collectstatic --no-input
  gunicorn billing.wsgi -w 4 -b 0.0.0.0:8000 --chdir=/app --log-file -
  echo "Production server running"
}

if [ ${PRODUCTION} == "false" ]; then
  start_development
else
  start_production
fi
