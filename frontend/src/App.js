import './App.css';
//imports React and hook usestate, state is used to store and manage state inside a functional component
//with React useState is used so that React remembers what the values of the variable is even after it rerenders the App
import React, {useState} from "react";

//Creates a functional component named 'App'
// export default means you can import it elsewhere as the default component
export default function App() {

  //this creates a constant state variable called message with initial value of "" empty string
  //setMessage is the function to update message
  //this will be used to hold the user input
  const [message, setMessage] = useState("");

  //constant state variable named chatHistory with initial value of [] empty array
  //setChatHistory is the function to update this array when a user inputs and ai outputs message
  const [chatHistory, setChatHistory] = useState([]);

  //this defines an asynchronous function called sendMessage
  const sendMessage = async () => {

    //this check if message is empty, if yes stops the function to prevent empty messages from being sent to frontend
    if (!message) return;

    //This is the function that updates chatHistory. It copies the current chatHistory using [...chatHistory, {...}] and inside the {...} is the new message that contains sender:"user" and text: message
    setChatHistory([...chatHistory, {sender: "user", text: message }]);

    //This sends the post request to the API and sets the response of API to the response variable
    //fetch is used to call the API using http request
    //await is used to pause execution until request is completed
    //method is the method of the request e.g. GET, POST, UPDATE
    //headers is the one that tells the server the data is in what format. in this example its json
    //body is the body of the request
    const response = await fetch("http://127.0.0.1:8000/api/chat", {
      
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({message}),

    });

    //this parses the response into json and sets it to the data variable e.g. { aireply: "AI said this" }
    const data = await response.json();

    //same as above setChatHistory but this appends the AI response
    setChatHistory((prev) => [...prev, {sender: "FranzAI", text: data.reply}]);
    
    //this function set the message variable to blank
    setMessage("");

  };

  return (
    
    <div className='min-h-screen flex items-center justify-center bg-botBg'>
      {/* this: min-h-screen flex items-center justify-center bg-gray-100 centers everything on screen with light gray background  */}
      {/* this: w-full max-w-md bg-white shadow-lg rounded-2xl p-6 this makes a white card with rounded corners and shadow  */}
      <div className='w-full max-w-7xl bg-[#202123] shadow-lg rounded-2xl p-6'>
        
        <h1 className="text-botAccent text-2xl font-bold text-center mb-4">Franz's Chatbot</h1>
        {/* this: h-80 overflow-y-auto border border-gray-300 rounded-lg p-3 mb-4 this keeps chat at a fixed height and has scrolls if too long  */}
        <div className='h-96 overflow-y-auto border border-gray-300 rounded-lg p-3 mb-4 bg-[#2a2b32]'>     
          {/* this code loops through chat history and for each chat, creates a div with key i and inside is the message from user and AI  */}
          {/* this also creates a div with class flex and checks if sender is user if yes justify end is used meaning it will be on the right side and if not user it will be justfiy start which means it will be on the left */}
          {chatHistory.map((chat, i) => (
            <div 
              key={i}
              className={`flex my-2 ${
                chat.sender === "user"
                ? "justify-end"
                : "justify-start"
              }`}
            >
              <div
                className={`px-4 py-2 rounded-2xl max-w-[70%] text-white ${
                  chat.sender === "user" ? "bg-botUser" : "bg-botBot"
                }`}
              >
                {chat.text}
              </div>
            </div>
          ))}

        </div>

        <div className='flex'>

          {/* this code is a textbox that when there is a change sets the message variable of whatever is inside the textbox  */}
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Type your message..."
            className='flex-grow border rounded-l-lg px-3 py-2 bg-[#40414f] text-white focus:outline-none focus:ring-2 focus:ring-botAccent'
          />
          <button
            onClick={sendMessage}
            className='bg-botAccent text-white px-4 py-2 rounded-r-lg hover:bg-emerald-600'
          >
            Send
          </button>

        </div>

      </div>

    </div>

  );

}

