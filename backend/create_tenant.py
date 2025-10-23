import argparse
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Tenant, User, UserRole
from auth_utils import get_password_hash

def create_tenant(db: Session, tenant_name: str, admin_email: str, admin_password: str):
    """
    Creates a new tenant and an admin user for that tenant.
    """
    try:
        # Check if tenant already exists
        existing_tenant = db.query(Tenant).filter(Tenant.name == tenant_name).first()
        if existing_tenant:
            print(f"❌ Tenant '{tenant_name}' already exists.")
            return

        # Check if admin email is already in use
        existing_user = db.query(User).filter(User.email == admin_email).first()
        if existing_user:
            print(f"❌ User with email '{admin_email}' already exists.")
            return

        # 1. Create the new tenant
        new_tenant = Tenant(name=tenant_name)
        db.add(new_tenant)
        db.commit()
        db.refresh(new_tenant)
        print(f"✅ Tenant '{new_tenant.name}' created successfully with ID: {new_tenant.id}")

        # 2. Create the admin user for the new tenant
        hashed_password = get_password_hash(admin_password)
        admin_user = User(
            tenant_id=new_tenant.id,
            email=admin_email,
            password_hash=hashed_password,
            role=UserRole.admin,
            is_active=True,
            first_name="Admin", # You can change this
            last_name=tenant_name # You can change this
        )
        db.add(admin_user)
        db.commit()
        db.refresh(admin_user)
        print(f"✅ Admin user '{admin_user.email}' created successfully for tenant '{new_tenant.name}'.")

    except Exception as e:
        db.rollback()
        print(f"❌ An error occurred: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new tenant and admin user.")
    parser.add_argument("--tenant", required=True, help="The name of the new tenant.")
    parser.add_argument("--email", required=True, help="The email for the admin user.")
    parser.add_argument("--password", required=True, help="The password for the admin user.")
    args = parser.parse_args()

    db = SessionLocal()
    create_tenant(db, args.tenant, args.email, args.password)
