# CLAUDE.md - AI Assistant Guide

## Project Overview

This is a Django 4.1.7 sample project demonstrating integration with **Strawberry GraphQL** and **Django Channels** for real-time WebSocket subscriptions. The project includes a classic polls application (Django tutorial steps 1-7) alongside a GraphQL API.

## Tech Stack

- **Framework**: Django 4.1.7
- **GraphQL**: Strawberry GraphQL (`strawberry.django`)
- **ASGI Server**: Daphne
- **WebSockets**: Django Channels
- **Database**: PostgreSQL
- **Language**: Python 3.x
- **Localization**: Korean (ko-kr), Asia/Seoul timezone

## Project Structure

```
django-strawberry-sample/
├── mysite/                 # Main Django project configuration
│   ├── settings.py         # Django settings (DB, apps, middleware)
│   ├── urls.py             # Root URL configuration
│   ├── asgi.py             # ASGI config with WebSocket routing
│   └── wsgi.py             # WSGI config (not used with Daphne)
├── polls/                  # Django polls application (tutorial)
│   ├── models.py           # Question and Choice models
│   ├── views.py            # Class-based views (ListView, DetailView)
│   ├── urls.py             # URL patterns for polls
│   ├── admin.py            # Admin configuration with inlines
│   ├── tests.py            # Unit tests for models and views
│   └── templates/polls/    # HTML templates
├── api/                    # GraphQL API application
│   ├── schema.py           # Strawberry GraphQL schema (Query, Mutation, Subscription)
│   └── urls.py             # GraphQL endpoint routing
├── templates/              # Global templates
│   └── admin/              # Admin template overrides
└── manage.py               # Django management script
```

## Key Components

### Polls App (`polls/`)
- **Models**: `Question` (with `was_published_recently()` method), `Choice`
- **Views**: Generic class-based views - `IndexView`, `DetailView`, `ResultsView`, `vote()`
- **URL namespace**: `polls`
- Routes: `/polls/`, `/polls/<id>/`, `/polls/<id>/results/`, `/polls/<id>/vote/`

### GraphQL API (`api/`)
- **Endpoint**: `/graphql/` (with subscriptions enabled)
- **WebSocket**: `/graphql` (via Channels)
- **Schema** (`api/schema.py`):
  - `Query.hello` - Returns "world"
  - `Mutation.add_book(title, author)` - Returns a Book object
  - `Subscription.count(target)` - Async generator counting to target

## Development Commands

```bash
# Run development server (uses Daphne for ASGI/WebSocket support)
python manage.py runserver

# Database migrations
python manage.py makemigrations
python manage.py migrate

# Run tests
python manage.py test
python manage.py test polls          # Test specific app

# Create superuser for admin
python manage.py createsuperuser

# Django shell
python manage.py shell
```

## Database Configuration

The project uses PostgreSQL (configured in `mysite/settings.py:82-91`):
- Database: `nexmond`
- User: `nexmond`
- Host: `localhost:5432`

**Note**: For development, you may need to update database credentials or switch to SQLite.

## URL Endpoints

| Path | Description |
|------|-------------|
| `/` | Root (includes api.urls) |
| `/graphql/` | GraphQL playground and API |
| `/polls/` | Polls index page |
| `/polls/<id>/` | Poll detail |
| `/polls/<id>/results/` | Poll results |
| `/polls/<id>/vote/` | Vote submission |
| `/admin/` | Django admin interface |

## Testing

Tests are located in `polls/tests.py` and cover:
- Model tests for `Question.was_published_recently()`
- View tests for index, detail pages
- Filtering of future-dated questions

Run with: `python manage.py test polls`

## Code Conventions

### Python Style
- Follow PEP 8 style guidelines
- Use class-based views for Django views where appropriate
- Models use descriptive `__str__` methods

### Django Patterns
- Use `app_name` in URL configs for namespacing
- Use `@admin.display` decorator for model admin customizations
- Generic views inherit from `django.views.generic`

### GraphQL (Strawberry)
- Use `@strawberry.type` for GraphQL types
- Use `@strawberry.field`, `@strawberry.mutation`, `@strawberry.subscription` decorators
- Async generators for subscriptions with `AsyncGenerator` typing

## Important Files for AI Assistants

When modifying this project, pay attention to:

1. **`mysite/settings.py`** - App registration, database config, middleware
2. **`mysite/urls.py`** - Root URL routing
3. **`mysite/asgi.py`** - WebSocket routing for GraphQL subscriptions
4. **`api/schema.py`** - GraphQL schema definitions
5. **`polls/models.py`** - Database models
6. **`polls/views.py`** - View logic

## Notes

- The admin interface is customized with Korean title ("투표 관리자")
- DEBUG is set to True (development only)
- ALLOWED_HOSTS is empty (development only)
- The SECRET_KEY in settings is for development only - use environment variables in production
