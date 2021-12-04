from sqlalchemy import Column, DateTime, Integer, String, text,Boolean,ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from api.session import AsyncSessionLocal

Base = declarative_base()

async def get_db() -> AsyncSessionLocal:
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()


class Blog(Base):
    __tablename__ = "blog"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(String(1000), nullable=False)
    is_deleted = Column(Boolean,nullable=False, default=False)
    ctime = Column(
        DateTime(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    mtime = Column(
        DateTime(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )

class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True)
    blog_id = Column(ForeignKey(Blog.id), nullable=False)
    comment = Column(String(1000), nullable=False)
    is_deleted = Column(Boolean,nullable=False, default=False)
    ctime = Column(
        DateTime(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    mtime = Column(
        DateTime(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
