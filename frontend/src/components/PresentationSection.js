
// PresentationSection handles displaying loading spinner, error messages, and the generated slides

import React from "react";
import { Box, Typography, CircularProgress } from "@mui/material";
import PresentationViewer from "./PresentationViewer";

const PresentationSection = ({ loading, error, slides }) => {
  // Show loading state with spinner and message
  if (loading) {
    return (
      <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', mt: 4 }}>
        <CircularProgress />
        <Typography variant="body2" sx={{ mt: 2 }}>
          Generating your presentation...
        </Typography>
      </Box>
    );
  }

  // Display error message if present
  if (error) {
    return (
      <Box sx={{ color: 'red', textAlign: 'center', mt: 4 }}>
        <Typography variant="body2">{error}</Typography>
      </Box>
    );
  }

  // Render slides if available
  if (slides && slides.length > 0) {
    return (
      <Box sx={{ textAlign: 'center', mt: 4 }}>
        <Typography variant="h6" sx={{ mb: 2 }}>
          Your presentation is ready!
        </Typography>
        <PresentationViewer slides={slides} />
      </Box>
    );
  }

  // Render nothing if no state is active
  return null;
};

export default PresentationSection;
