## Django Blog Platform - Dockerized Deployment

A production-ready blog platform with REST API, built with Django and deployed using Docker. Demonstrates three-tier architecture with Nginx reverse proxy, application server, PostgreSQL database, and Redis cache.

## Architecture Overview

- **Nginx** serves static/media files and proxies requests
- **Django + Gunicorn** handles application logic
- **PostgreSQL** stores persistent data
- **Redis** is used as a cache (AOF persistence enabled)
- Services are isolated using frontend and backend Docker networks.

## Key Features

### Application

- Django Admin for content management
- REST API using Django REST Framework
- Authentication & authorization
- Blog posts, categories, tags, comments
- Image uploads (media handling)

### Infrastructure

- Multi-stage Docker builds (optimized image size)
- Docker Compose orchestration (4 services)
- Named volumes for persistent data
- Health checks for PostgreSQL and Redis
- Non-root container execution (security)
- Redis AOF persistence
- Automatic migrations & static collection via entrypoint

## Challenges & solutions

1. **Static & Media File Sharing**

- Django writes files to shared Docker volumes
- Nginx mounts the same volumes as read-only
- Solved permission issues using runtime UID-based ownership

2. **Docker Volume Permission Issues**

- Volumes are created as root by Docker
- Entrypoint script fixes ownership at container startup
- Ensures Django can write and Nginx can safely read

3. **Safe Service Startup Order**

- PostgreSQL & Redis expose health checks
- Django waits until dependencies are healthy, not just started

4. **Secure Container Execution**

- Django runs as a non-root user (UID 1000)
- No build tools included in runtime image
- Read-only volume mounts for Nginx

5. **Optimized Docker Images**

- Dependencies compiled in builder stage
- Runtime image contains only wheels
- Smaller, faster, and more secure image

## Getting Started

1. **Clone Repository**
```bash
git clone https://github.com/nihmaltk/django-blog-docker.git
cd django-blog-docker
```

2. **Configure Environment**
```bash
# Copy environment template
cp .env.example .env
# Edit .env with your values
```

3. **Build and Deploy**

```bash
# Build images
docker-compose build

# Start all services
docker-compose up -d

# Check status
docker-compose ps
```
4. **Initialize Application**
```bash
# Create superuser
docker-compose exec django python manage.py createsuperuser
```

5. **Access Application**

**Admin Panel**: `http://your-server-ip/admin/`

**REST API**: `http://your-server-ip/api/`

**Health Check**: `http://your-server-ip/health`

## Technologies Used

- **Django + Django REST Framework**
- **Gunicorn**
- **PostgreSQL**
- **Redis (AOF persistence)**
- **Nginx**
- **Docker & Docker Compose**

## Security & Best Practices

- Non-root containers
- Network isolation (frontend/backend)
- Read-only mounts where applicable
- No secrets committed to code 
- Health checks for service readiness

## Key Concepts Demonstrated

- Real-world Docker & Compose usage
- Understanding of Linux permissions & UIDs
- Production-style Django deployment
- Reverse proxy & static file optimization
- Stateful services with persistence
- Clean separation of concerns

