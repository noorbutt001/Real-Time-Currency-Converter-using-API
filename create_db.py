from models import Base
from db_manager import engine

Base.metadata.create_all(bind=engine)

print("Database Created Successfully")