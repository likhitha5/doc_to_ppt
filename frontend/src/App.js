import React, { useState } from "react";
import axios from "axios";
import Header from "./components/Header";
import FileUploader from "./components/FileUploader";
import ModelSelector from "./components/ModelSelector";
import AudienceSelector from "./components/AudienceSelector";
import InstructionsInput from "./components/InstructionsInput";
import SubmitButton from "./components/SubmitButton";
import PresentationSection from "./components/PresentationSection";

import API_BASE_URL from "./config";

function App() {
  // State variables to manage form inputs and API response
  const [slides, setSlides] = useState([]);
  const [file, setFile] = useState(null);
  const [model, setModel] = useState("gemini");
  const [audienceType, setAudienceType] = useState("general");
  const [instructions, setInstructions] = useState("Generate an engaging presentation.");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Handles form submission and API request to backend
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file) {
      alert("Please select a file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("model", model);
    formData.append("audience_type", audienceType);
    formData.append("instructions", instructions);

    try {
      setLoading(true);
      setError(null);

      // Send data to backend and receive generated slides
      console.log(model);
      const response = await axios.post(`${API_BASE_URL}/upload`, formData);
      if (response.data && response.data.slides) {
        setSlides(response.data.slides);
      } else {
        setError("No slides data received.");
      }
    } catch (error) {
      // Handle various error cases
      if (error.response) {
        setError(`Error: ${error.response.data.detail || error.response.statusText}`);
      } else {
        setError("Error generating presentation. Please try again.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <Header />
      {/* Form for selecting model, audience, instructions, and uploading a file */}
      <form onSubmit={handleSubmit}>
        <ModelSelector model={model} setModel={setModel} />
        <AudienceSelector audienceType={audienceType} setAudienceType={setAudienceType} />
        <InstructionsInput instructions={instructions} setInstructions={setInstructions} />
        <FileUploader file={file} setFile={setFile} />
        <SubmitButton />
      </form>

      {/* Section to render the generated presentation or any error/loading state */}
      <PresentationSection loading={loading} error={error} slides={slides} />
    </div>
  );
}

export default App;
