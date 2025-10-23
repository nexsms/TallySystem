from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

# User Schemas
class UserBase(BaseModel):
    email: EmailStr
    username: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    role: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

# County, Constituency, and Ward Schemas
class WardBase(BaseModel):
    name: str
    constituency_id: int

class WardCreate(WardBase):
    pass

class WardResponse(WardBase):
    id: int

    class Config:
        from_attributes = True

class ConstituencyBase(BaseModel):
    name: str
    county_id: int

class ConstituencyCreate(ConstituencyBase):
    pass

class ConstituencyResponse(ConstituencyBase):
    id: int
    wards: List[WardResponse] = []

    class Config:
        from_attributes = True

class CountyBase(BaseModel):
    name: str

class CountyCreate(CountyBase):
    pass

class CountyResponse(CountyBase):
    id: int
    constituencies: List[ConstituencyResponse] = []

    class Config:
        from_attributes = True


# Tally Schemas
class TallyBase(BaseModel):
    location: str
    constituency_id: int
    ward_id: int
    votes_count: int
    total_registered_voters: Optional[int] = None
    notes: Optional[str] = None

class TallyCreate(TallyBase):
    pass

class TallyUpdate(BaseModel):
    location: Optional[str] = None
    votes_count: Optional[int] = None
    status: Optional[str] = None
    notes: Optional[str] = None

class TallyResponse(TallyBase):
    id: int
    status: str
    turnout_percentage: Optional[float] = None
    created_by: int
    created_at: datetime
    updated_at: datetime
    constituency: ConstituencyResponse
    ward: WardResponse

    class Config:
        from_attributes = True

# Auth Schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Dashboard Schemas
class DashboardStats(BaseModel):
    total_votes: int
    total_locations: int
    verified_tallies: int
    pending_tallies: int
    average_turnout: float
    top_constituencies: list


# Voter Schemas
class VoterBase(BaseModel):
    first_name: str
    last_name: str
    phone_number: Optional[str] = None
    ward_code: int
    ward_name: Optional[str] = None
    polling_station_name: Optional[str] = None


class VoterCreate(VoterBase):
    pass


class VoterResponse(VoterBase):
    id: str
    tenant_id: str
    middle_name: Optional[str] = None
    county_code: Optional[int] = None
    county_name: Optional[str] = None
    constituency_code: Optional[int] = None
    constituency_name: Optional[str] = None
    polling_station_code: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
