from sqlalchemy import (
    Column,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    Text,
)
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


# ============================================================
# 1️⃣ TENANTS TABLE
# ============================================================
class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(String, primary_key=True, index=True)  # National ID if applicable
    name = Column(String, nullable=False)
    position = Column(String)
    region = Column(String)
    logo_url = Column(String)

    # Relationships
    users = relationship("User", back_populates="tenant")
    voters = relationship("Voter", back_populates="tenant")
    agents = relationship("Agent", back_populates="tenant")
    incidents = relationship("Incident", back_populates="tenant")
    messages = relationship("Message", back_populates="tenant")
    audit_logs = relationship("AuditLog", back_populates="tenant")


# ============================================================
# 2️⃣ USERS TABLE
# ============================================================
class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)  # National ID
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    first_name = Column(String, nullable=False)
    middle_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String)
    role = Column(String, default="user")  # admin, coordinator, agent, etc.
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    tenant = relationship("Tenant", back_populates="users")
    audit_logs = relationship("AuditLog", back_populates="user")


# ============================================================
# 3️⃣ COUNTY / CONSTITUENCY / WARD (Hierarchy)
# ============================================================
class County(Base):
    __tablename__ = "counties"

    id = Column(String, primary_key=True, index=True)  # IEBC county code
    name = Column(String, unique=True, nullable=False)

    constituencies = relationship("Constituency", back_populates="county")


class Constituency(Base):
    __tablename__ = "constituencies"

    id = Column(String, primary_key=True, index=True)  # IEBC constituency code
    name = Column(String, nullable=False)
    county_id = Column(String, ForeignKey("counties.id"), nullable=False)

    county = relationship("County", back_populates="constituencies")
    wards = relationship("Ward", back_populates="constituency")


class Ward(Base):
    __tablename__ = "wards"

    id = Column(String, primary_key=True, index=True)  # IEBC ward code
    name = Column(String, nullable=False)
    constituency_id = Column(String, ForeignKey("constituencies.id"), nullable=False)

    constituency = relationship("Constituency", back_populates="wards")
    voters = relationship("Voter", back_populates="ward")
    agents = relationship("Agent", back_populates="ward")


# ============================================================
# 4️⃣ VOTERS TABLE
# ============================================================
class Voter(Base):
    __tablename__ = "voters"

    id = Column(String, primary_key=True, index=True)  # National ID
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)

    id_number = Column(String, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    last_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)

    county_code = Column(String, nullable=True)
    county_name = Column(String, nullable=True)
    constituency_code = Column(String, nullable=True)
    constituency_name = Column(String, nullable=True)
    ward_code = Column(String, nullable=True)
    ward_name = Column(String, nullable=True)
    polling_station_code = Column(String, nullable=True)
    polling_station_name = Column(String, nullable=True)

    tenant = relationship("Tenant", back_populates="voters")
    ward = relationship("Ward", back_populates="voters")


# ============================================================
# 5️⃣ AGENTS TABLE
# ============================================================
class Agent(Base):
    __tablename__ = "agents"

    id = Column(String, primary_key=True, index=True)  # National ID
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    role = Column(String, default="field_agent")
    status = Column(String, default="active")

    ward_id = Column(String, ForeignKey("wards.id"))
    polling_station_name = Column(String)

    tenant = relationship("Tenant", back_populates="agents")
    ward = relationship("Ward", back_populates="agents")


# ============================================================
# 6️⃣ INCIDENTS TABLE
# ============================================================
class Incident(Base):
    __tablename__ = "incidents"

    id = Column(String, primary_key=True, index=True)
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    description = Column(Text)
    ward_name = Column(String)
    status = Column(String, default="open")
    reported_by = Column(String)
    assigned_to = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    tenant = relationship("Tenant", back_populates="incidents")


# ============================================================
# 7️⃣ MESSAGES TABLE
# ============================================================
class Message(Base):
    __tablename__ = "messages"

    id = Column(String, primary_key=True, index=True)
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    message_text = Column(Text)
    target_group = Column(String)
    delivery_status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)

    tenant = relationship("Tenant", back_populates="messages")


# ============================================================
# 8️⃣ AUDIT LOGS TABLE
# ============================================================
class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(String, primary_key=True, index=True)
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    user_id = Column(String, ForeignKey("users.id"), nullable=True)
    action = Column(String)
    module = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    tenant = relationship("Tenant", back_populates="audit_logs")
    user = relationship("User", back_populates="audit_logs")
