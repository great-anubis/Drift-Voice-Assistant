import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000/api';

export const generateText = async (inputText) => {
    try {
        const response = await axios.post(`${API_URL}/generate`, { text: inputText });
        return response.data;
    } catch (error) {
        console.error("Error generating text:", error);
        throw error;
    }
};
