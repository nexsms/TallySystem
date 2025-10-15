from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import get_db
from models import User, Tally
from schemas import DashboardStats
from auth_utils import get_current_active_user

router = APIRouter()

@router.get("/stats", response_model=DashboardStats)
async def get_dashboard_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    # Total votes
    total_votes = db.query(func.sum(Tally.votes_count)).scalar() or 0
    
    # Total locations
    total_locations = db.query(Tally).count()
    
    # Verified tallies
    verified_tallies = db.query(Tally).filter(Tally.status == "verified").count()
    
    # Pending tallies
    pending_tallies = db.query(Tally).filter(Tally.status == "pending").count()
    
    # Average turnout
    avg_turnout = db.query(func.avg(Tally.turnout_percentage)).scalar() or 0.0
    
    # Top constituencies by votes
    top_constituencies = db.query(
        Tally.constituency,
        func.sum(Tally.votes_count).label("total_votes")
    ).group_by(Tally.constituency).order_by(func.sum(Tally.votes_count).desc()).limit(5).all()
    
    top_constituencies_list = [
        {"constituency": c[0], "votes": c[1]} for c in top_constituencies if c[0]
    ]
    
    return {
        "total_votes": total_votes,
        "total_locations": total_locations,
        "verified_tallies": verified_tallies,
        "pending_tallies": pending_tallies,
        "average_turnout": round(avg_turnout, 2),
        "top_constituencies": top_constituencies_list
    }
