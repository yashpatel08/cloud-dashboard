import { useEffect, useState } from "react";
import type { Resource, Recommendation } from "../types";
import axios from "axios";
import Summary from "../components/Summary";
import ResourceTable from "../components/ResourceTable";
import Recommendations from "../components/Recommendations";

export default function Dashboard() {
    const [resources, setResources] = useState<Resource[]>([]);
    const [recommendations, setRecommendations] = useState<Recommendation[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {
        const fetchData = async () => {
            try {
                const res = await axios.get<Resource[]>("http://localhost:8000/resources");
                const recs = await axios.get<Recommendation[]>("http://localhost:8000/recommendations");
                setResources(res.data);
                setRecommendations(recs.data);
                setLoading(false);
            } catch (err) {
                setError("Failed to fetch data");
                setLoading(false);
            }
        };
        fetchData();
    }, []);

    const handleImplement = async (id: number, implemented: boolean) => {
        if (implemented) return;
        try {
            await axios.patch(`http://localhost:8000/recommendations/${id}/implement`);
            const updated = await axios.get<Recommendation[]>("http://localhost:8000/recommendations");
            setRecommendations(updated.data);
        } catch (err) {
            console.error("Error implementing recommendation:", err);
        }
    };

    const totalMonthlyCost = resources.reduce((sum, r) => sum + r.monthly_cost, 0);
    const totalSavings = recommendations.reduce((sum, r) => sum + r.estimated_savings, 0);

    if (loading) return <div className="p-4">Loading...</div>;
    if (error) return <div className="p-4 text-red-500">{error}</div>;

    return (
        <div className="p-6 space-y-6">
            <h1 className="text-3xl font-bold text-white mb-6">Cloud Optimization Dashboard</h1>
            <Summary
                resourceCount={resources.length}
                totalCost={totalMonthlyCost}
                totalSavings={totalSavings}
                opportunityCount={recommendations.length}
            />
            <ResourceTable resources={resources} />
            <Recommendations recommendations={recommendations} onImplement={handleImplement} />
        </div>
    );
}
