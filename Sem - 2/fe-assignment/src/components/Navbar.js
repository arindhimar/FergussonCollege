"use client"
import { AppBar, Toolbar, Typography, InputBase, IconButton, Box, useTheme, alpha } from "@mui/material"
import SearchIcon from "@mui/icons-material/Search"
import Brightness4Icon from "@mui/icons-material/Brightness4"
import Brightness7Icon from "@mui/icons-material/Brightness7"
import LocalMoviesIcon from "@mui/icons-material/LocalMovies"

export default function Navbar({ mode, toggleTheme, onSearch, searchQuery }) {
  const theme = useTheme()

  return (
    <AppBar
      position="sticky"
      elevation={4}
      sx={{
        borderRadius: 0,
        background:
          theme.palette.mode === "dark"
            ? "linear-gradient(90deg, #0f172a 0%, #1e293b 100%)"
            : "linear-gradient(90deg, #0ea5e9 0%, #38bdf8 100%)",
      }}
    >
      <Toolbar sx={{ display: "flex", justifyContent: "space-between" }}>
        <Box sx={{ display: "flex", alignItems: "center" }}>
          <LocalMoviesIcon sx={{ mr: 1, fontSize: 28 }} />
          <Typography variant="h6" noWrap sx={{ fontWeight: "bold", letterSpacing: "0.5px" }}>
            Movie Explorer
          </Typography>
        </Box>

        <Box sx={{ display: "flex", alignItems: "center", gap: 2 }}>
          <Box
            sx={{
              position: "relative",
              backgroundColor: alpha(theme.palette.common.white, 0.15),
              borderRadius: "24px",
              px: 2,
              py: 0.5,
              display: "flex",
              alignItems: "center",
              transition: "all 0.3s",
              "&:hover": {
                backgroundColor: alpha(theme.palette.common.white, 0.25),
              },
            }}
          >
            <SearchIcon />
            <InputBase
              placeholder="Quick search…"
              sx={{
                ml: 1,
                color: "inherit",
                width: { xs: "120px", sm: "200px" },
              }}
              value={searchQuery}
              onChange={onSearch}
            />
          </Box>

          <IconButton
            onClick={toggleTheme}
            color="inherit"
            sx={{
              bgcolor: alpha(theme.palette.common.white, 0.1),
              "&:hover": {
                bgcolor: alpha(theme.palette.common.white, 0.2),
              },
            }}
          >
            {mode === "dark" ? <Brightness7Icon /> : <Brightness4Icon />}
          </IconButton>
        </Box>
      </Toolbar>
    </AppBar>
  )
}
