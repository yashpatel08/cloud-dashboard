from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    resource_type = Column(String, nullable=False)
    provider = Column(String, nullable=False)
    instance_type = Column(String, nullable=True)
    size_gb = Column(Integer, nullable=True)
    cpu_utilization = Column(Float, nullable=True)
    memory_utilization = Column(Float, nullable=True)
    storage_usage_gb = Column(Integer, nullable=True)
    monthly_cost = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    recommendations = relationship("Recommendation", back_populates="resource")


class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)
    resource_id = Column(Integer, ForeignKey("resources.id", ondelete="CASCADE"))
    recommendation_text = Column(String)
    potential_savings = Column(Float)
    implemented = Column(Boolean, default=False)
    confidence = Column(String, default="low")

    # inverse key
    resource = relationship("Resource", back_populates="recommendations")
