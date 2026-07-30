from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

# GET /users/me is implemented in the next step.
