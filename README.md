# Little Lemon Restaurant — Full Stack Meta Assessment

## 🚀 What is this?
A Django web app for the Little Lemon restaurant that lets users browse menu items and create table reservations from the website. It also exposes booking data through JSON endpoints used by the reservation UI.

## 🎯 Problem it solves
The project provides a single place for a restaurant to present its menu and manage table bookings by date and time slot. It was built as the final assessment project for the Meta Full Stack course.

## ✨ Key Features
- Public restaurant pages: home, about, menu, and booking.
- Reservation form with live availability by selected date.
- Time-slot conflict prevention when creating bookings.
- JSON endpoints for listing bookings and creating new reservations.
- Django admin integration for managing booking and menu records.

## 🛠 Tech Stack
- Python 3.13
- Django 4.x
- MySQL (via `mysqlclient`)
- HTML templates + vanilla JavaScript + CSS
- Pipenv

## ⚡ Quick Start
```bash
# 1) Install dependencies
pipenv install

# 2) Create .env (example values)
cat > .env << 'ENV'
SECRET_KEY=replace-with-your-secret-key
DEBUG=True
DATABASE_NAME=littlelemon
DATABASE_USER=your-db-user
DATABASE_PASSWORD=your-db-password
DATABASE_HOST=localhost
DATABASE_PORT=3306
ALLOWED_HOSTS=127.0.0.1,localhost
ENV

# 3) Apply migrations
pipenv run python manage.py migrate

# 4) Run the app
pipenv run python manage.py runserver
```

## 📦 Scripts
- `pipenv run python manage.py runserver` — start local dev server.
- `pipenv run python manage.py migrate` — apply database migrations.
- `pipenv run python manage.py createsuperuser` — create admin user.
- `pipenv run python manage.py test` — run test suite.

## 📌 Notes
- The app reads all sensitive configuration from environment variables in `.env`; do not commit `.env`.
- The default database backend is MySQL, configured in `littlelemon/settings.py`.
- Main booking routes:
  - `GET /reservations/?date=YYYY-MM-DD` — booking list for a date.
  - `GET /bookings?date=YYYY-MM-DD` and `POST /bookings` — booking API used by the booking page.
