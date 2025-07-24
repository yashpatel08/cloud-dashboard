export interface Resource {
    id: number;
    name: string;
    resource_type: string;
    provider: string;
    instance_type?: string;
    size_gb?: number;
    cpu_utilization?: number;
    memory_utilization?: number;
    storage_usage_gb?: number;
    monthly_cost: number;
    created_at?: string;
    updated_at?: string;
}

export interface Recommendation {
    resource_id: number;
    name: string;
    reason: string;
    current_cost: number;
    estimated_savings: number;
}
