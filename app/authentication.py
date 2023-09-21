from app.models import User
from app.database import SessionLocal

def authenticate_user(username: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    db.close()
    return user

# Additional authentication logic can be added here
