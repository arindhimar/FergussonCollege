'use client';
import { AppBar, Toolbar, Typography, InputBase, IconButton, Box, Switch } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import Brightness4Icon from '@mui/icons-material/Brightness4';
import Brightness7Icon from '@mui/icons-material/Brightness7';

export default function Navbar({ mode, toggleTheme }) {
  return (
    <AppBar position="sticky" elevation={4} sx={{ borderRadius: 2 }}>
      <Toolbar sx={{ display: 'flex', justifyContent: 'space-between' }}>
        <Typography variant="h6" noWrap sx={{ fontWeight: 'bold' }}>
          🎬 Movie Explorer
        </Typography>

        <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
          <Box
            sx={{
              position: 'relative',
              backgroundColor: 'rgba(255,255,255,0.15)',
              borderRadius: 1,
              px: 2,
              py: 0.5,
              display: 'flex',
              alignItems: 'center',
            }}
          >
            <SearchIcon />
            <InputBase placeholder="Search…" sx={{ ml: 1, color: 'inherit' }} />
          </Box>

          <IconButton onClick={toggleTheme} color="inherit">
            {mode === 'dark' ? <Brightness7Icon /> : <Brightness4Icon />}
          </IconButton>
        </Box>
      </Toolbar>
    </AppBar>
  );
}
