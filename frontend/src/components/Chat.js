import React, { useState } from 'react';

const Chat = () => {
  const [messages, setMessages] = useState([]);

  const handleSend = () => {
    // Handle sending messages
  };

  return (
    <div className="chat-container">
      <div className="messages">
        {messages.map((msg, index) => (
          <div key={index} className="message">{msg}</div>
        ))}
      </div>
      <input type="text" className="message-input" />
      <button onClick={handleSend} className="send-button">Send</button>
    </div>
  );
};

export default Chat;
