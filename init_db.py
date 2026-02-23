from database import Base, engine,SessionLocal
import models

Base.metadata.create_all(bind=engine)

db = SessionLocal()

db.add_all([
    models.User(name="Alice",email="alice@example.com",role="admin"),
    models.User(name="Bob",email="bob@example.com",role="user"),
    models.User(name="Cara",email="cara@example.com",role="admin")

])
db.commit()
db.close()

print("DB initialised with sample data !!!")