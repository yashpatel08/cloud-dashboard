import type { Resource } from "../types";

interface Props {
    resources: Resource[];
}

export default function ResourceTable({ resources }: Props) {
    return (
        <div>
            <h2 className="text-xl font-semibold mb-2">Cloud Resources</h2>
            <div className="overflow-auto">
                <table className="min-w-full divide-y divide-gray-700 rounded-lg overflow-hidden">
                    <thead className="bg-gray-900 text-gray-300">
                        <tr>
                            <th className="p-2">Name</th>
                            <th className="p-2">Type</th>
                            <th className="p-2">Provider</th>
                            <th className="p-2">CPU</th>
                            <th className="p-2">Memory</th>
                            <th className="p-2">Cost</th>
                        </tr>
                    </thead>
                    <tbody className="bg-gray-800 divide-y divide-gray-700 text-center">
                        {resources.map((r) => (
                            <tr key={r.id} className="hover:bg-gray-700 transition duration-150 ease-in-out">
                                <td className="p-2">{r.name}</td>
                                <td className="p-2">{r.resource_type}</td>
                                <td className="p-2">{r.provider}</td>
                                <td className="p-2">
                                    {r.resource_type === 'storage' ? (
                                        <span className="px-2 py-1 rounded-full text-sm font-medium bg-blue-600 text-white">
                                            {r.storage_usage ? `${r.storage_usage}GB` : r.size ? `${r.size}GB` : "-"}
                                        </span>
                                    ) : (
                                        <span className={`px-2 py-1 rounded-full text-sm font-medium 
                                            ${r.cpu_utilization != null && r.cpu_utilization < 30
                                                ? "bg-yellow-600 text-white"
                                                : "bg-green-600 text-white"}`}>
                                            {r.cpu_utilization != null ? `${r.cpu_utilization}%` : "-"}
                                        </span>
                                    )}
                                </td>
                                <td className="p-2">
                                    {r.resource_type === 'storage' ? (
                                        <span className="text-gray-400">-</span>
                                    ) : (
                                        <span className={`px-2 py-1 rounded-full text-sm font-medium 
                                            ${r.memory_utilization != null && r.memory_utilization < 50
                                                ? "bg-yellow-600 text-white"
                                                : "bg-green-600 text-white"}`}>
                                            {r.memory_utilization != null ? `${r.memory_utilization}%` : "-"}
                                        </span>
                                    )}
                                </td>
                                <td className="p-2">${r.monthly_cost}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}