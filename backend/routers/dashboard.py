from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import get_db
from models import User
from schemas import DashboardStats
from auth_utils import get_current_active_user, get_tenant_id

router = APIRouter()

@router.get("/stats", response_model=DashboardStats)
async def get_dashboard_stats(
    db: Session = Depends(get_db),
    tenant_id: str = Depends(get_tenant_id),
    current_user: User = Depends(get_current_active_user),
):
    # Placeholder data since Tally model is removed
    total_votes = 0
    total_locations = 0
    verified_tallies = 0
    pending_tallies = 0
    avg_turnout = 0.0
    top_constituencies_list = []

    return {
        "total_votes": total_votes,
        "total_locations": total_locations,
        "verified_tallies": verified_tallies,
        "pending_tallies": pending_tallies,
        "average_turnout": round(avg_turnout, 2),
        "top_constituencies": top_constituencies_list,
    }

