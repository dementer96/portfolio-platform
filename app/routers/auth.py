from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])

# POST /auth/register and POST /auth/login are implemented in the next step.
