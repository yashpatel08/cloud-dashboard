import type { Recommendation } from "../types";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

interface Props {
  recommendations: Recommendation[];
  onImplement: (id: number, implemented: boolean) => void;
}

export default function Recommendations({ recommendations, onImplement }: Props) {
  return (
    <div>
      <h2 className="text-xl font-semibold mb-2">Optimization Recommendations</h2>
      <div className="grid gap-4 md:grid-cols-3">
        {recommendations.map((rec) => (
          <Card
            key={rec.resource_id}
            className="border-l-4 border-blue-500 bg-gray-800 text-white shadow rounded-lg w-120"
          >
            <CardContent className="p-4 bg-gray-800 text-white space-y-2">
              <div className="text-lg font-bold">{rec.name}</div>
              <div className="text-sm text-gray-300">{rec.reason}</div>
              <div className="text-sm">
                💰 Current Cost: <span className="text-white">${rec.current_cost}</span>
              </div>
              <div className="text-sm">
                💡 Estimated Savings:{" "}
                <span className="text-green-400">${rec.estimated_savings}</span>
              </div>
              <div className="text-sm">
                📊 Confidence: <span className="capitalize">{rec.confidence}</span>
              </div>
              <Button
                onClick={() => onImplement(rec.id, rec.implemented)}
                disabled={rec.implemented}
                className={`mt-2 w-full ${rec.implemented
                    ? "bg-green-700 cursor-not-allowed"
                    : "bg-blue-600 hover:bg-blue-700"
                  } text-white`}
              >
                {rec.implemented ? "✅ Implemented" : "Mark as Implemented"}
              </Button>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
