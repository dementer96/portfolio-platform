from sqlalchemy import Column, DateTime, Index, Integer, String
from sqlalchemy.sql import func

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    __table_args__ = (
        # Case-insensitive uniqueness: enforced at the DB level so it holds
        # even if a caller bypasses the UserCreate schema's normalization.
        Index("ix_users_email_lower", func.lower(email), unique=True),
    )
