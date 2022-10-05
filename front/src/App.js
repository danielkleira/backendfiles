import logo from "./logo.svg";
import "./App.css";
import { useEffect, useState } from "react";
import { api } from "./api/api";

function App() {
  const [selectedFile, setSelectedFile] = useState();
  useEffect(()=>{
    api.post("/file/", selectedFile)
  },[selectedFile])
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <form>
          <input type="file" value={selectedFile} onChange={(e)=> setSelectedFile(e.target.files[0])}/>
        </form>
      </header>
    </div>
  );
}

export default App;
