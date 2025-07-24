from fastapi import APIRouter, Depends, HTTPException, status   
from sqlalchemy.orm import Session

from app.database import get_db
from typing import List
from app.models import Resource, Recommendation
from datetime import datetime
from app.schemas import ResourceOut, ResourceCreate, RecommendationOut

router = APIRouter()

# Get all resources
@router.get("/resources", response_model=List[ResourceOut])
def get_resources_with_recommendations(db: Session = Depends(get_db)):
    resources = db.query(Resource).all()

    result = []
    for res in resources:
        recs_out = []
        for rec in res.recommendations:
            recs_out.append({
                "id": rec.id,
                "reason": rec.recommendation_text,
                "estimated_savings": rec.potential_savings,
                "current_cost": res.monthly_cost,
                "implemented": rec.implemented,
                "resource_id": rec.resource_id,
                "name": res.name,
            })

        result.append({
            "id": res.id,
            "name": res.name,
            "resource_type": res.resource_type,
            "provider": res.provider,
            "instance_type": res.instance_type,
            "size_gb": res.size_gb,
            "cpu_utilization": res.cpu_utilization,
            "memory_utilization": res.memory_utilization,
            "storage_usage_gb": res.storage_usage_gb,
            "monthly_cost": res.monthly_cost,
            "recommendations": recs_out,
        })

    return result

@router.post("/resources", response_model=ResourceOut, status_code=status.HTTP_201_CREATED)
def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    db_resource = Resource(
        name=resource.name,
        resource_type=resource.resource_type,
        provider=resource.provider,
        instance_type=resource.instance_type,
        size_gb=resource.size_gb,
        cpu_utilization=resource.cpu_utilization,
        memory_utilization=resource.memory_utilization,
        storage_usage_gb=resource.storage_usage_gb,
        monthly_cost=resource.monthly_cost,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

# Get optimization recommendations
@router.get("/recommendations", response_model=List[RecommendationOut])
def get_recommendations(db: Session = Depends(get_db)):
    recs = db.query(Recommendation).all()
    results = []
    for r in recs:
        results.append({
            "id": r.id,
            "reason": r.recommendation_text,
            "estimated_savings": r.potential_savings,
            "current_cost": r.resource.monthly_cost if r.resource else 0,
            "implemented": r.implemented,
            "resource_id": r.resource_id,
            "name": r.resource.name if r.resource else "Unknown",
            "confidence": r.confidence
        })
    return results

@router.patch("/recommendations/{rec_id}/implement")
def implement_recommendation(rec_id: int, db: Session = Depends(get_db)):
    rec = db.query(Recommendation).filter(Recommendation.id == rec_id).first()
    if not rec:
        raise HTTPException(status_code=404, detail="Recommendation not found")
    rec.implemented = True
    db.commit()
    return {"message": "Recommendation marked as implemented"}