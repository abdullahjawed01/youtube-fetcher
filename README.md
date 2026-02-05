# 📺 YouTube Video Fetcher Backend

A production-ready backend service built using Django and Django REST Framework that continuously fetches the latest YouTube videos for a given search query, stores them in a PostgreSQL database, and exposes APIs to list and search videos efficiently.

The system uses Celery for background processing, Redis as a message broker, and Docker for containerized deployment.

---

## 🚀 Core Features

- Fetch latest YouTube videos using YouTube Data API v3
- Background ingestion using Celery workers
- Periodic scheduling with Celery Beat
- Store video metadata in PostgreSQL
- REST APIs to list videos in reverse chronological order
- Full-text search on title and description
- Pagination support
- Admin dashboard for database inspection
- Fully Dockerized setup
- Scalable and production-ready architecture

---

## 🛠 Tech Stack

- Python 3.11
- Django
- Django REST Framework
- PostgreSQL
- Celery
- Celery Beat
- Redis
- Gunicorn
- Docker & Docker Compose

---

## 📂 Project Structure

```
src/
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   ├── wsgi.py
│   └── celery.py
├── videos/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tasks.py
├── manage.py
docker/
├── django.Dockerfile
├── celery.Dockerfile
├── celery-beat.Dockerfile
docker-compose.yml
requirements.txt
README.md
```

---

## 📡 Data Model

Each video record contains:

- video_id (unique)
- title
- description
- published_at
- thumbnail_url
- channel_title
- created_at

Duplicate videos are avoided using a unique constraint on `video_id`.

---

## 🌐 API Endpoints

### List Videos

```
GET /api/videos/
```

- Returns videos sorted by published_at (descending)
- Paginated response

---

### Search Videos

```
GET /api/videos/search/?q=tea
```

- Full-text search on title and description
- Case-insensitive
- Paginated response

---

### Admin Panel

```
http://localhost:8000/admin/
```

---

## ⚙️ Environment Variables

Create a `.env` file in the project root:

```env
DEBUG=1
SECRET_KEY=your-secret-key
YOUTUBE_API_KEY=your-youtube-api-key

POSTGRES_DB=youtube
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

REDIS_HOST=redis
REDIS_PORT=6379
```

---

## 🐳 Docker Setup

### Build and Start Services

```bash
docker compose up --build
```

---

### Run Database Migrations

```bash
docker compose exec web python manage.py migrate
```

---

### Create Admin User

```bash
docker compose exec web python manage.py createsuperuser
```

---

## 🔁 Background Processing

- Celery workers fetch YouTube videos asynchronously
- Celery Beat schedules periodic fetch jobs
- Redis is used as the message broker
- API failures and duplicates are handled gracefully

---

## 🏗 Production Readiness

- Gunicorn used as WSGI server
- Settings split for development and production
- Environment-based configuration
- Containerized services for scalability
- Clean separation of concerns

---

## 👨‍💻 Author

Abdullah  
Full stack Developer

GitHub: https://github.com/abdullahjawed01 


---

## 📜 License

MIT License

This project is free to use, modify, and distribute.

---

## 🙏 Acknowledgements

- YouTube Data API
- Django & Django REST Framework
- Celery
- Docker
