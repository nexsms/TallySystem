from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    role = Column(String, default="user")  # admin, coordinator, agent, user
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    tallies = relationship("Tally", back_populates="created_by_user")

class County(Base):
    __tablename__ = "counties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)

    constituencies = relationship("Constituency", back_populates="county")

class Constituency(Base):
    __tablename__ = "constituencies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    county_id = Column(Integer, ForeignKey("counties.id"))

    county = relationship("County", back_populates="constituencies")
    wards = relationship("Ward", back_populates="constituency")
    tallies = relationship("Tally", back_populates="constituency")

class Ward(Base):
    __tablename__ = "wards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    constituency_id = Column(Integer, ForeignKey("constituencies.id"))

    constituency = relationship("Constituency", back_populates="wards")
    tallies = relationship("Tally", back_populates="ward")

class Tally(Base):
    __tablename__ = "tallies"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, nullable=False)  # Polling station or area
    constituency_id = Column(Integer, ForeignKey("constituencies.id"))
    ward_id = Column(Integer, ForeignKey("wards.id"))
    votes_count = Column(Integer, default=0)
    total_registered_voters = Column(Integer)
    turnout_percentage = Column(Float)
    status = Column(String, default="pending")  # pending, verified, disputed
    notes = Column(Text)
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    created_by_user = relationship("User", back_populates="tallies")
    constituency = relationship("Constituency", back_populates="tallies")
    ward = relationship("Ward", back_populates="tallies")

class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    candidate_name = Column(String, default="Hon. Philip Aroko")
    position = Column(String)
    election_date = Column(DateTime)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
