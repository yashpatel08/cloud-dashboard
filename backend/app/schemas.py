from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ResourceBase(BaseModel):
    name: str
    resource_type: str
    provider: str
    instance_type: Optional[str] = None
    size_gb: Optional[float] = None
    cpu_utilization: Optional[float] = None
    memory_utilization: Optional[float] = None
    storage_usage_gb: Optional[float] = None
    monthly_cost: float


class ResourceCreate(ResourceBase):
    pass

class RecommendationBase(BaseModel):
    recommendation_text: str
    potential_savings: float
    implemented: bool = False
    confidence: Optional[str] = "low"


class RecommendationCreate(RecommendationBase):
    resource_id: int

class RecommendationOut(BaseModel):
    id: int
    reason: str
    estimated_savings: float
    current_cost: float
    implemented: bool
    resource_id: int
    name: str 
    confidence: Optional[str] = "low"
    
    class Config:
        orm_mode = True

class ResourceOut(ResourceBase):
    id: int
    recommendations: List[RecommendationOut] = []

    class Config:
        orm_mode = True