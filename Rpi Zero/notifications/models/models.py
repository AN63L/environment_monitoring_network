# ORM models
from sqlalchemy import Column, Integer, String, TIMESTAMP, text

from db.connection import Base


#### NOTIFICATIONS Log TABLE ###


class NotificationsLog(Base):
    __tablename__ = "notifications_log"

    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False, index=True)
    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=text("now()"),
        nullable=False,
        index=True,
    )

    __table_args__ = {"schema": "metrics"}
