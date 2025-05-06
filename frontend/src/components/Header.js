
// Top navigation bar displaying the title of the application

import React from "react";
import { AppBar, Toolbar, Typography, Box } from "@mui/material";

const Header = () => (
  <Box sx={{ flexGrow: 1, marginBottom: 6 }}>
    <AppBar position="static" sx={{ backgroundColor: 'primary.dark' }}>
      <Toolbar>
        <Typography variant="h6" sx={{ flexGrow: 1 }}>
          Document to Presentation Converter - AI Powered
        </Typography>
      </Toolbar>
    </AppBar>
  </Box>
);

export default Header;
