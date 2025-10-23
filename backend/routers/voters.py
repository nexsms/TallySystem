from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import User, Voter
from schemas import VoterResponse
from auth_utils import get_current_active_user, get_tenant_id

router = APIRouter()

@router.get("/", response_model=List[VoterResponse])
async def get_voters(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    tenant_id: str = Depends(get_tenant_id),
    current_user: User = Depends(get_current_active_user),
):
    voters = (
        db.query(Voter)
        .filter(Voter.tenant_id == tenant_id)
        .offset(skip)
        .limit(limit)
        .all()
    )
    return voters
