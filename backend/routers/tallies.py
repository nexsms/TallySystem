from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import User, Tally
from schemas import TallyCreate, TallyResponse, TallyUpdate
from auth_utils import get_current_active_user

router = APIRouter()

@router.post("/", response_model=TallyResponse, status_code=status.HTTP_201_CREATED)
async def create_tally(
    tally: TallyCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    # Calculate turnout percentage if possible
    turnout_percentage = None
    if tally.total_registered_voters and tally.total_registered_voters > 0:
        turnout_percentage = (tally.votes_count / tally.total_registered_voters) * 100
    
    new_tally = Tally(
        **tally.model_dump(),
        created_by=current_user.id,
        turnout_percentage=turnout_percentage
    )
    
    db.add(new_tally)
    db.commit()
    db.refresh(new_tally)
    
    return new_tally

@router.get("/", response_model=List[TallyResponse])
async def get_tallies(
    skip: int = 0,
    limit: int = 100,
    status: str = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    query = db.query(Tally)
    
    if status:
        query = query.filter(Tally.status == status)
    
    tallies = query.offset(skip).limit(limit).all()
    return tallies

@router.get("/{tally_id}", response_model=TallyResponse)
async def get_tally(
    tally_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    tally = db.query(Tally).filter(Tally.id == tally_id).first()
    
    if not tally:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tally not found"
        )
    
    return tally

@router.put("/{tally_id}", response_model=TallyResponse)
async def update_tally(
    tally_id: int,
    tally_update: TallyUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    tally = db.query(Tally).filter(Tally.id == tally_id).first()
    
    if not tally:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tally not found"
        )
    
    # Update fields
    update_data = tally_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(tally, field, value)
    
    db.commit()
    db.refresh(tally)
    
    return tally

@router.delete("/{tally_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tally(
    tally_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    tally = db.query(Tally).filter(Tally.id == tally_id).first()
    
    if not tally:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tally not found"
        )
    
    # Only admin or creator can delete
    if current_user.role != "admin" and tally.created_by != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this tally"
        )
    
    db.delete(tally)
    db.commit()
    
    return None
