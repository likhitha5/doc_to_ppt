
// Dropdown to select the GenAI model (e.g., OpenAI, Gemini, Hugging Face)

import React from "react";
import { FormControl, InputLabel, MenuItem, Select, Box } from "@mui/material";

const ModelSelector = ({ model, setModel }) => (
  <Box sx={{ minWidth: 120, marginBottom: 2 }}>
    <FormControl fullWidth>
      <InputLabel>Choose Gen AI Model</InputLabel>
      <Select
  value={model}
  onChange={(e) => setModel(e.target.value)}
  label="Choose Gen AI Model"
>
  <MenuItem value={"gemini"}>Gemini</MenuItem>
  <MenuItem value={"openai"} disabled>
    OpenAI (coming soon)
  </MenuItem>
  <MenuItem value={"huggingface"} disabled>
    Hugging Face (coming soon)
  </MenuItem>
</Select>
    </FormControl>
  </Box>
);

export default ModelSelector;
