# SecureOps Intelligence Platform

A portfolio project for AppSec / DevSecOps / Cloud Security roles, built
incrementally in phases rather than all at once. See [PROJECT.md](PROJECT.md)
for the full brief, current phase, and explicit non-goals — this README only
covers what's actually implemented and how to run it.

## Current stack

- **Backend:** Python 3.12 + FastAPI
- **Database:** PostgreSQL, run via Docker Compose
- **ORM:** SQLAlchemy, tables created on app startup via
  `Base.metadata.create_all()` (no Alembic migrations yet)
- **Auth:** Hand-rolled JWT (PyJWT) + bcrypt password hashing — no Entra ID
  or OAuth yet
- **Containerization:** Docker + Docker Compose (API + Postgres)
- **Frontend:** none — API only, exercised through FastAPI's auto-generated
  docs at `/docs`

## What's implemented

- `POST /auth/register` — create a user (email + password)
- `POST /auth/login` — verify credentials, returns a JWT access token
- `GET /users/me` — protected endpoint, requires a valid bearer token,
  returns the current user

Everything else in PROJECT.md's target stack (cloud deployment, CI/CD,
frontend UI, AI/RAG features, Entra ID/OAuth) is planned but not built yet.

## Setup

1. Copy `.env.example` to `.env` and fill in real values (at minimum, change
   `JWT_SECRET_KEY`). Never commit your `.env`.

   ```bash
   cp .env.example .env
   ```

2. Start the API and Postgres:

   ```bash
   docker compose up
   ```

3. Open [http://localhost:8000/docs](http://localhost:8000/docs).

4. Try the flow:
   - `POST /auth/register` with an email and password to create a user.
   - `POST /auth/login` with the same credentials to get an access token.
   - Click **Authorize** in `/docs` (or set the `Authorization: Bearer
     <token>` header manually) and call `GET /users/me` to confirm it
     returns your user.
