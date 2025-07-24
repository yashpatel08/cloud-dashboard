from app.models import Base, Resource, Recommendation
from app.database import engine, SessionLocal
from datetime import datetime

def generate_recommendation(resource: Resource) -> Recommendation | None:
    # Rule 1: Over-provisioned instance
    if resource.resource_type == "instance" and (resource.cpu_utilization or 0) < 30 and (resource.memory_utilization or 0) < 50:
        return Recommendation(
            resource_id=resource.id,
            recommendation_text="Over-provisioned instance. Recommend downsizing.",
            potential_savings=round(resource.monthly_cost * 0.3, 2),
            implemented=False,
            confidence="high"
        )

    # Rule 2: Large storage volumes
    elif resource.resource_type == "storage" and (resource.size_gb or 0) > 500:
        return Recommendation(
            resource_id=resource.id,
            recommendation_text="Large storage volume. Recommend reducing size.",
            potential_savings=round(resource.monthly_cost * 0.25, 2),
            implemented=False,
            confidence="medium"
        )

    return None

def init_db():
    # Create all tables
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()

    # Avoid duplicate seeding
    if session.query(Resource).first():
        print("Database already seeded.")
        return

    now = datetime.now()

    resources = [
        Resource(name="web-server-1", resource_type="instance", provider="AWS",
                 instance_type="t3.xlarge", cpu_utilization=15.0, memory_utilization=25.0,
                 monthly_cost=150.0, created_at=now, updated_at=now),
        Resource(name="api-server-2", resource_type="instance", provider="AWS",
                 instance_type="m5.large", cpu_utilization=12.0, memory_utilization=30.0,
                 monthly_cost=90.0, created_at=now, updated_at=now),
        Resource(name="worker-3", resource_type="instance", provider="Azure",
                 instance_type="Standard_D2s_v3", cpu_utilization=8.0, memory_utilization=20.0,
                 monthly_cost=70.0, created_at=now, updated_at=now),

        Resource(name="database-1", resource_type="instance", provider="AWS",
                 instance_type="m5.xlarge", cpu_utilization=75.0, memory_utilization=85.0,
                 monthly_cost=180.0, created_at=now, updated_at=now),
        Resource(name="cache-server", resource_type="instance", provider="GCP",
                 instance_type="n1-standard-2", cpu_utilization=65.0, memory_utilization=70.0,
                 monthly_cost=50.0, created_at=now, updated_at=now),

        Resource(name="backup-storage", resource_type="storage", provider="AWS",
                 size_gb=1000, storage_usage_gb=1000, monthly_cost=100.0,
                 created_at=now, updated_at=now),
        Resource(name="log-storage", resource_type="storage", provider="Azure",
                 size_gb=500, storage_usage_gb=500, monthly_cost=75.0,
                 created_at=now, updated_at=now),

        Resource(name="database-storage", resource_type="storage", provider="GCP",
                 size_gb=200, storage_usage_gb=200, monthly_cost=25.0,
                 created_at=now, updated_at=now),
    ]

    for r in resources:
        session.add(r)
        session.commit()

        rec = generate_recommendation(r)
        if rec:
            session.add(rec)
            session.commit()

    session.close()
    print("✅ Database seeded successfully with recommendations.")

if __name__ == "__main__":
    init_db()
