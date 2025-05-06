
// SubmitButton component renders a styled submit button using MUI

import React from "react";
import { Box, Button } from "@mui/material";

const SubmitButton = () => (
  <Box sx={{ mb: 2 }}>
    <Button type="submit" variant="contained">
      Generate Presentation
    </Button>
  </Box>
);

export default SubmitButton;
