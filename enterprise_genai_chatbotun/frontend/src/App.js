
import React, { useState } from "react";
import axios from "axios";

function App() {
  const [msg, setMsg] = useState("");
  const [chat, setChat] = useState([]);

  const send = async () => {
    const res = await axios.post("http://localhost:8000/chat", {question: msg});
    setChat([...chat, {q: msg, a: res.data.response}]);
    setMsg("");
  };

  return (
    <div>
      <h2>Marketing Chatbot</h2>
      <input value={msg} onChange={e=>setMsg(e.target.value)} />
      <button onClick={send}>Send</button>
      {chat.map((c,i)=>(
        <div key={i}>
          <b>You:</b> {c.q}<br/>
          <b>Bot:</b> {c.a}
        </div>
      ))}
    </div>
  );
}

export default App;
