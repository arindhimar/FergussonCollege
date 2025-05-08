// app/layout.js
'use client';

import { CssBaseline, ThemeProvider } from '@mui/material';
import { createTheme } from '@mui/material/styles';

const theme = createTheme();

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <title>My MUI App</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </head>
      <body>
        <ThemeProvider theme={theme}>
          <CssBaseline />
          {children}
        </ThemeProvider>
      </body>
    </html>
  );
}
