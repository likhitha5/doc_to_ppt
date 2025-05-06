// File upload component allowing users to select a PDF for presentation generation

import React, { useState } from "react";
import { Box, Button, Typography, Alert } from "@mui/material";
import CloudUploadIcon from '@mui/icons-material/CloudUpload';

const FileUploader = ({ file, setFile }) => {
  const [error, setError] = useState(null);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile && selectedFile.type !== "application/pdf") {
      setError("Only PDF files are supported.");
      setFile(null); // Clear the file state if it's not a PDF
    } else {
      setError(null);
      setFile(selectedFile);
    }
  };

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 2, mb: 2, minWidth: 300 }}>
      <Button component="label" variant="contained" startIcon={<CloudUploadIcon />} sx={{ minWidth: 150 }}>
        Upload PDF
        <input
          hidden
          type="file"
          accept="application/pdf"
          onChange={handleFileChange}
        />
      </Button>
      <Typography variant="body2">
        {file ? `Selected file: ${file.name}` : 'No file chosen (PDF only)'}
      </Typography>
      {error && <Alert severity="error">{error}</Alert>}
    </Box>
  );
};

export default FileUploader;
