from database import engine, Base
from models import (
    Tenant,
    User,
    County,
    Constituency,
    Ward,
    Voter,
    Agent,
    Incident,
    Message,
    AuditLog,
)

def main():
    print("Dropping all tables...")
    Base.metadata.drop_all(bind=engine)
    print("Creating all tables...")
    Base.metadata.create_all(bind=engine)
    print("Database reset complete.")

if __name__ == "__main__":
    main()