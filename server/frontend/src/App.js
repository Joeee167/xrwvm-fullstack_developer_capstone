import LoginPanel from "./components/Login/Login";
import RegisterPanel from "./components/Register/Register"; // Import the correct component for registration
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<RegisterPanel />} /> {/* Correct component for registration */}
    </Routes>
  );
}

export default App;
