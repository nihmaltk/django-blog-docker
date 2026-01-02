#!/bin/sh

set -e 

echo "Starting Django application..."

# Fix permissions for volume mount points
if [ "$(id -u)" = "0" ]; then
    echo "Running as root, fixing ownership..."
    
    mkdir -p /app/staticfiles /app/media
    
    chown -R django:django /app/staticfiles /app/media
    
    echo "Running migrations and collecting static files..."

    gosu django python manage.py migrate --noinput
    gosu django python manage.py collectstatic --noinput

    echo "Switching to django user to start server..."
    exec gosu django "$@"
else
    echo "Running as django user"
    exec "$@"
fi