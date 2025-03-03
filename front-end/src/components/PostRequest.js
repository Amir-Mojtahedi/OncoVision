import { useState } from 'react';
import axios from 'axios';

function PostRequest() {
  const [responseMessage, setResponseMessage] = useState('');

  const handlePostRequest = async () => {
    const data = {
      name: 'AI model',
      message:
        'Later on, we will send actual data to the AI model that is deployed on our backend',
    };

    try {
      const response = await axios.post(
        'http://127.0.0.1:5000/api/ai-model',
        data
      );
      setResponseMessage(`Success: ${JSON.stringify(response.data)}`);
    } catch (error) {
      setResponseMessage(
        `Error: ${error.response ? error.response.data : error.message}`
      );
    }
  };

  return (
    <div>
      <h2>Send POST Request to Flask</h2>
      <button onClick={handlePostRequest}>Send Request</button>
      <p>{responseMessage}</p>
    </div>
  );
}

export default PostRequest;
