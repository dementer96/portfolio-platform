# SecureOps Intelligence Platform (pippado.com)

## What this is
A single, evolving security platform built as a portfolio piece for AppSec /
DevSecOps / Cloud Security roles. Modules are added incrementally — this file
only describes the CURRENT phase. Do not build ahead of it.

## Target stack
- Backend: Python 3.12 + FastAPI
- Database: PostgreSQL (via Docker Compose locally)
- ORM: SQLAlchemy
- Auth: JWT (hand-rolled for now — no Entra ID yet, that's a later phase)
- Containerization: Docker + Docker Compose
- Frontend: none yet — API only, tested via FastAPI's auto docs (/docs)

## Non-goals for this phase (explicitly out of scope)
- No cloud deployment yet (local only)
- No CI/CD yet
- No frontend UI yet
- No AI/RAG features yet
- No Entra ID / OAuth yet
- Do not add extra endpoints, models, or "nice to have" features beyond
  what's listed below. Small and correct beats broad and half-done.

## CURRENT PHASE: Week 1 — Local scaffold

Goal: a running FastAPI app, backed by Postgres in Docker, with:
1. Project structure using best-practice FastAPI layout (app/, routers/,
   models/, schemas/, core/, etc.)
2. A `User` model: id, email (unique), hashed_password, created_at
3. `POST /auth/register` — creates a user, hashes password (passlib/bcrypt)
4. `POST /auth/login` — verifies credentials, returns a JWT access token
5. `GET /users/me` — protected endpoint, requires valid JWT, returns the
   current user
6. `docker-compose.yml` running the API + Postgres together
7. `.env.example` for config (DB URL, JWT secret) — never commit a real `.env`
8. A short README with setup instructions (clone, docker compose up, hit
   /docs)

## Working style
- Explain the reasoning behind auth/security decisions, not just the code —
  I'm rebuilding my Python skills, not outsourcing them.
- Prefer standard, well-known libraries over custom implementations.
- Keep commits small and message them clearly (this repo is a portfolio
  piece — commit history should read as a coherent build log).

## Definition of done for this phase
`docker compose up` starts both containers, `/docs` loads, I can register
a user, log in, and hit /users/me with the returned token. Nothing else.
