
// Dropdown component for selecting the target audience type for the presentation

import React from "react";
import { FormControl, InputLabel, MenuItem, Select, Box } from "@mui/material";

const AudienceSelector = ({ audienceType, setAudienceType }) => (
  <Box sx={{ minWidth: 120, marginBottom: 2 }}>
    <FormControl fullWidth>
      <InputLabel>Choose Audience Type</InputLabel>
      <Select value={audienceType} onChange={(e) => setAudienceType(e.target.value) } label="Choose Audience Type">
      <MenuItem value={"general"}>General</MenuItem>
        <MenuItem value={"educational"}>Educational</MenuItem>
        <MenuItem value={"technical"}>Technical</MenuItem>
        <MenuItem value={"business"}>Business</MenuItem>
      </Select>
    </FormControl>
  </Box>
);

export default AudienceSelector;
