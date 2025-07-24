import axios from "axios";
import type { Resource, Recommendation } from "../types/index";

const BASE_URL = "http://localhost:8000/api/resources";

export const fetchResources = async (): Promise<Resource[]> => {
    const response = await axios.get(`${BASE_URL}/`);
    console.log("resource",response.data);
    return response.data;
};

export const fetchRecommendations = async (): Promise<Recommendation[]> => {
    const response = await axios.get(`${BASE_URL}/recommendations`);
    console.log("recommendations",response.data);
    return response.data;
};
