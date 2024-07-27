import React, { useState } from 'react';
import { generateText } from '../apiService';

const Chat = () => {
    const [input, setInput] = useState('');
    const [messages, setMessages] = useState([]);

    const handleSend = async () => {
        try {
            const response = await generateText(input);
            setMessages([...messages, { text: input, from: 'user' }, { text: response.response, from: 'bot' }]);
            setInput('');
        } catch (error) {
            console.error("Error sending message:", error);
        }
    };

    return (
        <div className="p-4">
            <div className="mb-4">
                {messages.map((msg, index) => (
                    <div key={index} className={`p-2 ${msg.from === 'user' ? 'bg-blue-100' : 'bg-gray-100'} my-2 rounded`}>
                        {msg.text}
                    </div>
                ))}
            </div>
            <input 
                className="border p-2 w-full"
                value={input} 
                onChange={(e) => setInput(e.target.value)} 
            />
            <button className="bg-purple-600 text-white p-2 mt-2" onClick={handleSend}>Enter</button>
        </div>
    );
    
};

export default Chat;
