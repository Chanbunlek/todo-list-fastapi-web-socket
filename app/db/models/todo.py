from app.db.models import *

class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True)
    todo = Column(String, nullable=False)
    is_completed = Column(Boolean, default=False)
    create_date = Column(DateTime, nullable=False, default=func.now())
