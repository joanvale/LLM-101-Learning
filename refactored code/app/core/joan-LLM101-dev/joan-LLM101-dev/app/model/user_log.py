# user_log.py

from sqlalchemy import Column, Integer, String, DateTime
from model.database import Base
from datetime import datetime

class UserLog(Base):
    __tablename__ = "user_logs"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    activity = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
