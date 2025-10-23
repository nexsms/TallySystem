import enum
import uuid
from sqlalchemy import (
    Column,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    Text,
    Enum,
)
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


def generate_uuid():
    return str(uuid.uuid4())


class BaseModel(Base):
    __abstract__ = True
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class UserRole(enum.Enum):
    admin = "admin"
    coordinator = "coordinator"
    agent = "agent"
    user = "user"


class AgentRole(enum.Enum):
    field_agent = "field_agent"


class AgentStatus(enum.Enum):
    active = "active"
    inactive = "inactive"


class IncidentStatus(enum.Enum):
    open = "open"
    closed = "closed"


class MessageDeliveryStatus(enum.Enum):
    pending = "pending"
    sent = "sent"
    failed = "failed"


# ============================================================
# 1️⃣ TENANTS TABLE
# ============================================================
class Tenant(BaseModel):
    __tablename__ = "tenants"

    id = Column(
        String, primary_key=True, index=True, default=generate_uuid
    )  # National ID or unique org code
    name = Column(String, nullable=False)
    position = Column(String)
    region = Column(String)
    logo_url = Column(String)

    # Relationships
    users = relationship("User", back_populates="tenant", cascade="all, delete-orphan")
    voters = relationship(
        "Voter", back_populates="tenant", cascade="all, delete-orphan"
    )
    agents = relationship(
        "Agent", back_populates="tenant", cascade="all, delete-orphan"
    )
    incidents = relationship(
        "Incident", back_populates="tenant", cascade="all, delete-orphan"
    )
    messages = relationship(
        "Message", back_populates="tenant", cascade="all, delete-orphan"
    )
    audit_logs = relationship(
        "AuditLog", back_populates="tenant", cascade="all, delete-orphan"
    )


# ============================================================
# 2️⃣ USERS TABLE
# ============================================================
class User(BaseModel):
    __tablename__ = "users"

    id = Column(
        String, primary_key=True, index=True, default=generate_uuid
    )  # National ID
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    first_name = Column(String, nullable=False)
    middle_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String)
    role = Column(Enum(UserRole), default=UserRole.user)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    tenant = relationship("Tenant", back_populates="users")
    audit_logs = relationship("AuditLog", back_populates="user")


# ============================================================
# 3️⃣ COUNTY TABLE
# ============================================================
class County(BaseModel):
    __tablename__ = "counties"

    id = Column(Integer, primary_key=True, index=True)  # IEBC county code
    name = Column(String, unique=True, nullable=False)

    constituencies = relationship(
        "Constituency", back_populates="county", cascade="all, delete-orphan"
    )


# ============================================================
# 4️⃣ CONSTITUENCY TABLE
# ============================================================
class Constituency(BaseModel):
    __tablename__ = "constituencies"

    id = Column(Integer, primary_key=True, index=True)  # IEBC constituency code
    name = Column(String, nullable=False)
    county_id = Column(Integer, ForeignKey("counties.id"), nullable=False)

    county = relationship("County", back_populates="constituencies")
    wards = relationship("Ward", back_populates="constituency", cascade="all, delete-orphan")


# ============================================================
# 5️⃣ WARD TABLE
# ============================================================
class Ward(BaseModel):
    __tablename__ = "wards"

    id = Column(Integer, primary_key=True, index=True)  # IEBC ward code
    name = Column(String, nullable=False)
    constituency_id = Column(Integer, ForeignKey("constituencies.id"), nullable=False)

    constituency = relationship("Constituency", back_populates="wards")
    agents = relationship("Agent", back_populates="ward", cascade="all, delete-orphan")


# ============================================================
# 6️⃣ VOTER TABLE
# ============================================================
class Voter(BaseModel):
    __tablename__ = "voters"

    id = Column(
        String, primary_key=True, index=True, default=generate_uuid
    )  # National ID
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)

    first_name = Column(String, nullable=False)
    middle_name = Column(String)
    last_name = Column(String, nullable=False)
    phone_number = Column(String)

    # Using ward_code instead of FK (for CSV compatibility)
    ward_code = Column(Integer, nullable=False)
    ward_name = Column(String)

    # Optional fields for analytics / redundancy
    county_code = Column(Integer)
    county_name = Column(String)
    constituency_code = Column(Integer)
    constituency_name = Column(String)
    polling_station_code = Column(String)
    polling_station_name = Column(String)

    tenant = relationship("Tenant", back_populates="voters")


# ============================================================
# 7️⃣ AGENT TABLE
# ============================================================
class Agent(BaseModel):
    __tablename__ = "agents"

    id = Column(
        String, primary_key=True, index=True, default=generate_uuid
    )  # National ID
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    first_name = Column(String, nullable=False)
    middle_name = Column(String)
    last_name = Column(String, nullable=False)
    phone_number = Column(String)
    role = Column(Enum(AgentRole), default=AgentRole.field_agent)
    status = Column(Enum(AgentStatus), default=AgentStatus.active)

    ward_id = Column(Integer, ForeignKey("wards.id"), nullable=False)
    polling_station_name = Column(String)

    tenant = relationship("Tenant", back_populates="agents")
    ward = relationship("Ward", back_populates="agents")


# ============================================================
# 8️⃣ INCIDENT TABLE
# ============================================================
class Incident(BaseModel):
    __tablename__ = "incidents"

    id = Column(String, primary_key=True, index=True, default=generate_uuid)
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    description = Column(Text)
    ward_name = Column(String)
    status = Column(Enum(IncidentStatus), default=IncidentStatus.open)
    reported_by = Column(String)
    assigned_to = Column(String)

    tenant = relationship("Tenant", back_populates="incidents")


# ============================================================
# 9️⃣ MESSAGE TABLE
# ============================================================
class Message(BaseModel):
    __tablename__ = "messages"

    id = Column(String, primary_key=True, index=True, default=generate_uuid)
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    message_text = Column(Text)
    target_group = Column(String)
    delivery_status = Column(
        Enum(MessageDeliveryStatus), default=MessageDeliveryStatus.pending
    )

    tenant = relationship("Tenant", back_populates="messages")


# ============================================================
# 🔟 AUDIT LOG TABLE
# ============================================================
class AuditLog(BaseModel):
    __tablename__ = "audit_logs"

    id = Column(String, primary_key=True, index=True, default=generate_uuid)
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    user_id = Column(String, ForeignKey("users.id"))
    action = Column(String)
    module = Column(String)

    tenant = relationship("Tenant", back_populates="audit_logs")
    user = relationship("User", back_populates="audit_logs")