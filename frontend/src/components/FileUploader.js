
// File upload component allowing users to select a document for presentation generation

import React from "react";
import { Box, Button, Typography } from "@mui/material";
import CloudUploadIcon from '@mui/icons-material/CloudUpload';

const FileUploader = ({ file, setFile }) => (
  <Box sx={{ display: 'flex', alignItems: 'center', gap: 2, mb: 2, minWidth: 300 }}>
    <Button component="label" variant="contained" startIcon={<CloudUploadIcon />} sx={{ minWidth: 150 }}>
      Upload File
      <input hidden type="file" onChange={(e) => setFile(e.target.files[0])} />
    </Button>
    <Typography variant="body2">
      {file ? `Selected file: ${file.name}` : 'No file chosen'}
    </Typography>
  </Box>
);

export default FileUploader;
