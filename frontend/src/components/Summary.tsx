import { Card, CardContent } from "@/components/ui/card";

interface SummaryProps {
    resourceCount: number;
    totalCost: number;
    totalSavings: number;
    opportunityCount: number;
}

export default function Summary({
    resourceCount,
    totalCost,
    totalSavings,
    opportunityCount,
}: SummaryProps) {
    return (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
            <Card className="bg-gradient-to-br from-gray-800 to-gray-900 text-white border border-gray-700 shadow-lg rounded-xl">
                <CardContent className="p-6 text-center text-lg font-medium">
                    Resources: {resourceCount}
                </CardContent>
            </Card>
            <Card className="bg-gradient-to-br from-gray-800 to-gray-900 text-white border border-gray-700 shadow-lg rounded-xl">
                <CardContent className="p-6 text-center text-lg font-medium">
                    Monthly Cost: ${totalCost.toFixed(2)}
                </CardContent>
            </Card>
            <Card className="bg-gradient-to-br from-gray-800 to-gray-900 text-white border border-gray-700 shadow-lg rounded-xl">
                <CardContent className="p-6 text-center text-lg font-medium">
                    Potential Savings: ${totalSavings.toFixed(2)}
                </CardContent>
            </Card>
            <Card className="bg-gradient-to-br from-gray-800 to-gray-900 text-white border border-gray-700 shadow-lg rounded-xl">
                <CardContent className="p-6 text-center text-lg font-medium">
                    Opportunities: {opportunityCount}
                </CardContent>
            </Card>
        </div>
    );
}