
// Text input field for users to provide custom instructions to guide the presentation generation

import React from "react";
import { FormControl, TextField, Box } from "@mui/material";

const InstructionsInput = ({ instructions, setInstructions }) => (
  <Box sx={{ minWidth: 120, mb: 2 }}>
    <FormControl fullWidth>
      <TextField
        label="Any specific instructions?"
        value={instructions}
        onChange={(e) => setInstructions(e.target.value)}
        fullWidth
        multiline
        minRows={1}
      />
    </FormControl>
  </Box>
);

export default InstructionsInput;
