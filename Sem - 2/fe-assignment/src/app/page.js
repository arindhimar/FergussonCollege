"use client"

import { useState, useEffect, useMemo } from "react"
import axios from "axios"
import {
  Box,
  Container,
  Grid,
  CssBaseline,
  ThemeProvider,
  CircularProgress,
  Typography,
  FormControl,
  Select,
  MenuItem,
  TextField,
  Slider,
  Chip,
  Paper,
  Stack,
  Divider,
  InputAdornment,
  useMediaQuery,
  Drawer,
  IconButton,
  Button,
  Tab,
  Tabs,
  alpha,
} from "@mui/material"
import { getTheme } from "../theme/theme"
import Navbar from "../components/Navbar"
import MovieCard from "../components/MovieCard"
import SearchIcon from "@mui/icons-material/Search"
import SortIcon from "@mui/icons-material/Sort"
import FilterListIcon from "@mui/icons-material/FilterList"
import CloseIcon from "@mui/icons-material/Close"
import TuneIcon from "@mui/icons-material/Tune"
import StarIcon from "@mui/icons-material/Star"

const GENRES = [
  "Action",
  "Adventure",
  "Animation",
  "Biography",
  "Comedy",
  "Crime",
  "Documentary",
  "Drama",
  "Family",
  "Fantasy",
  "History",
  "Horror",
  "Music",
  "Mystery",
  "Romance",
  "Sci-Fi",
  "Thriller",
  "War",
  "Western",
]

export default function HomePage() {
  const [mode, setMode] = useState("light")
  const theme = useMemo(() => getTheme(mode), [mode])
  const [movies, setMovies] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState("")
  const isMobile = useMediaQuery(theme.breakpoints.down("md"))
  const [drawerOpen, setDrawerOpen] = useState(false)
  const [activeTab, setActiveTab] = useState(0)

  const [searchQuery, setSearchQuery] = useState("")
  const [selectedGenres, setSelectedGenres] = useState([])
  const [ratingRange, setRatingRange] = useState([0, 10])
  const [sortBy, setSortBy] = useState("none")
  const [filteredMovies, setFilteredMovies] = useState([])

  useEffect(() => {
    async function fetchMovies() {
      try {
        const res = await axios.get("https://imdb236.p.rapidapi.com/imdb/lowest-rated-movies", {
          headers: {
            "x-rapidapi-key": "0cc3d8c429msh967ab5a4fb0a39ep1ec8d4jsnd29731211186",
            "x-rapidapi-host": "imdb236.p.rapidapi.com",
          },
        })

        const arr = Array.isArray(res.data) ? res.data : []

        const transformedMovies = arr.map((movie) => ({
          id: movie.id || `movie-${Math.random()}`,
          title: movie.primaryTitle || "Unknown Title",
          year: movie.startYear || "N/A",
          rating: movie.averageRating || 0,
          poster: movie.primaryImage || "/placeholder.svg?height=450&width=300",
          genres: movie.genres || ["Unknown"],
          description: movie.description || "No description available",
          duration: movie.runtime || null,
        }))

        setMovies(transformedMovies)
        setFilteredMovies(transformedMovies)
      } catch (e) {
        console.error(e)
        setError("Could not load movies")

        const sampleMovies = Array(12)
          .fill(0)
          .map((_, i) => ({
            id: `sample-${i}`,
            title: `Sample Movie ${i + 1}`,
            year: 2000 + Math.floor(Math.random() * 23),
            rating: (Math.random() * 10).toFixed(1),
            poster: movie.primaryImage || "/placeholder.svg?height=450&width=300",
            genres: [GENRES[Math.floor(Math.random() * GENRES.length)]],
            description: "This is a sample movie description.",
            duration: `${Math.floor(Math.random() * 3) + 1}h ${Math.floor(Math.random() * 59) + 1}m`,
          }))

        setMovies(sampleMovies)
        setFilteredMovies(sampleMovies)
      } finally {
        setLoading(false)
      }
    }
    fetchMovies()
  }, [])

  useEffect(() => {
    let result = [...movies]

    if (searchQuery) {
      const query = searchQuery.toLowerCase()
      result = result.filter(
        (movie) => movie.title.toLowerCase().includes(query) || movie.description.toLowerCase().includes(query),
      )
    }

    if (selectedGenres.length > 0) {
      result = result.filter((movie) => movie.genres && selectedGenres.some((genre) => movie.genres.includes(genre)))
    }

    result = result.filter((movie) => movie.rating >= ratingRange[0] && movie.rating <= ratingRange[1])

    switch (sortBy) {
      case "title-asc":
        result.sort((a, b) => a.title.localeCompare(b.title))
        break
      case "title-desc":
        result.sort((a, b) => b.title.localeCompare(a.title))
        break
      case "year-asc":
        result.sort((a, b) => a.year - b.year)
        break
      case "year-desc":
        result.sort((a, b) => b.year - a.year)
        break
      case "rating-asc":
        result.sort((a, b) => a.rating - b.rating)
        break
      case "rating-desc":
        result.sort((a, b) => b.rating - a.rating)
        break
      default:
        break
    }

    setFilteredMovies(result)
  }, [movies, searchQuery, selectedGenres, ratingRange, sortBy])

  const handleGenreChange = (event) => {
    const {
      target: { value },
    } = event
    setSelectedGenres(typeof value === "string" ? value.split(",") : value)
  }

  const handleRatingChange = (event, newValue) => {
    setRatingRange(newValue)
  }

  const handleSearch = (event) => {
    setSearchQuery(event.target.value)
  }

  const handleSortChange = (event) => {
    setSortBy(event.target.value)
  }

  const handleGenreDelete = (genreToDelete) => {
    setSelectedGenres(selectedGenres.filter((genre) => genre !== genreToDelete))
  }

  const toggleDrawer = () => {
    setDrawerOpen(!drawerOpen)
  }

  const clearAllFilters = () => {
    setSearchQuery("")
    setSelectedGenres([])
    setRatingRange([0, 10])
    setSortBy("none")
  }

  const handleTabChange = (event, newValue) => {
    setActiveTab(newValue)
  }

  const filterContent = (
    <Box sx={{ p: 3 }}>
      <Box sx={{ display: "flex", justifyContent: "space-between", alignItems: "center", mb: 3 }}>
        <Typography variant="h5" fontWeight="bold" sx={{ color: theme.palette.primary.main }}>
          Discover Movies
        </Typography>
        {isMobile && (
          <IconButton onClick={toggleDrawer} size="small" sx={{ color: theme.palette.primary.main }}>
            <CloseIcon />
          </IconButton>
        )}
      </Box>

      <Tabs
        value={activeTab}
        onChange={handleTabChange}
        variant="fullWidth"
        sx={{
          mb: 3,
          "& .MuiTab-root": {
            textTransform: "none",
            fontWeight: 600,
            fontSize: "0.95rem",
          },
          "& .Mui-selected": {
            color: theme.palette.primary.main,
          },
        }}
      >
        <Tab label="Search" icon={<SearchIcon />} iconPosition="start" />
        <Tab label="Filter" icon={<FilterListIcon />} iconPosition="start" />
        <Tab label="Sort" icon={<SortIcon />} iconPosition="start" />
      </Tabs>

      {activeTab === 0 && (
        <Box>
          <TextField
            fullWidth
            placeholder="Search by title or description..."
            variant="outlined"
            value={searchQuery}
            onChange={handleSearch}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <SearchIcon />
                </InputAdornment>
              ),
            }}
            sx={{
              "& .MuiOutlinedInput-root": {
                borderRadius: "12px",
                backgroundColor: alpha(theme.palette.background.paper, 0.6),
              },
            }}
          />
        </Box>
      )}

      {activeTab === 1 && (
        <Stack spacing={3}>
          <Box>
            <Typography variant="subtitle1" fontWeight="600" gutterBottom>
              Genres
            </Typography>
            <FormControl fullWidth>
              <Select
                multiple
                value={selectedGenres}
                onChange={handleGenreChange}
                displayEmpty
                renderValue={(selected) => {
                  if (selected.length === 0) {
                    return <Typography color="text.secondary">Select genres</Typography>
                  }
                  return (
                    <Box sx={{ display: "flex", flexWrap: "wrap", gap: 0.5 }}>
                      {selected.map((value) => (
                        <Chip
                          key={value}
                          label={value}
                          size="small"
                          onDelete={() => handleGenreDelete(value)}
                          onMouseDown={(event) => {
                            event.stopPropagation()
                          }}
                          sx={{
                            backgroundColor: theme.palette.primary.main,
                            color: "white",
                            fontWeight: 500,
                          }}
                        />
                      ))}
                    </Box>
                  )
                }}
                sx={{
                  borderRadius: "12px",
                  backgroundColor: alpha(theme.palette.background.paper, 0.6),
                }}
              >
                {GENRES.map((genre) => (
                  <MenuItem key={genre} value={genre}>
                    {genre}
                  </MenuItem>
                ))}
              </Select>
            </FormControl>
          </Box>

          <Box>
            <Typography
              variant="subtitle1"
              fontWeight="600"
              gutterBottom
              sx={{ display: "flex", alignItems: "center" }}
            >
              <StarIcon sx={{ mr: 1, color: "gold", fontSize: "1.2rem" }} />
              IMDb Rating: {ratingRange[0]} - {ratingRange[1]}
            </Typography>
            <Slider
              value={ratingRange}
              onChange={handleRatingChange}
              valueLabelDisplay="auto"
              min={0}
              max={10}
              step={0.5}
              sx={{
                color: theme.palette.primary.main,
                "& .MuiSlider-thumb": {
                  width: 16,
                  height: 16,
                },
              }}
            />
          </Box>
        </Stack>
      )}

      {activeTab === 2 && (
        <Box>
          <Typography variant="subtitle1" fontWeight="600" gutterBottom>
            Sort By
          </Typography>
          <FormControl fullWidth>
            <Select
              value={sortBy}
              onChange={handleSortChange}
              displayEmpty
              sx={{
                borderRadius: "12px",
                backgroundColor: alpha(theme.palette.background.paper, 0.6),
              }}
            >
              <MenuItem value="none">Default</MenuItem>
              <MenuItem value="title-asc">Title (A-Z)</MenuItem>
              <MenuItem value="title-desc">Title (Z-A)</MenuItem>
              <MenuItem value="year-asc">Year (Oldest First)</MenuItem>
              <MenuItem value="year-desc">Year (Newest First)</MenuItem>
              <MenuItem value="rating-asc">Rating (Low to High)</MenuItem>
              <MenuItem value="rating-desc">Rating (High to Low)</MenuItem>
            </Select>
          </FormControl>
        </Box>
      )}

      <Button
        variant="contained"
        color="primary"
        onClick={clearAllFilters}
        fullWidth
        sx={{
          mt: 3,
          borderRadius: "12px",
          textTransform: "none",
          fontWeight: "bold",
          py: 1.2,
          boxShadow: "0 4px 12px rgba(0,0,0,0.15)",
        }}
      >
        Clear All Filters
      </Button>

      {(selectedGenres.length > 0 || searchQuery || ratingRange[0] > 0 || ratingRange[1] < 10 || sortBy !== "none") && (
        <Box sx={{ mt: 3 }}>
          <Divider sx={{ my: 2 }} />
          <Typography variant="body2" fontWeight="500" color="text.secondary">
            Active Filters:
          </Typography>
          <Stack direction="row" spacing={1} sx={{ mt: 1, flexWrap: "wrap", gap: 1 }}>
            {searchQuery && (
              <Chip
                label={`Search: ${searchQuery}`}
                onDelete={() => setSearchQuery("")}
                size="small"
                sx={{
                  backgroundColor: alpha(theme.palette.primary.main, 0.1),
                  color: theme.palette.primary.main,
                  fontWeight: 500,
                }}
              />
            )}
            {selectedGenres.map((genre) => (
              <Chip
                key={genre}
                label={`Genre: ${genre}`}
                onDelete={() => handleGenreDelete(genre)}
                size="small"
                sx={{
                  backgroundColor: alpha(theme.palette.primary.main, 0.1),
                  color: theme.palette.primary.main,
                  fontWeight: 500,
                }}
              />
            ))}
            {(ratingRange[0] > 0 || ratingRange[1] < 10) && (
              <Chip
                label={`Rating: ${ratingRange[0]} - ${ratingRange[1]}`}
                onDelete={() => setRatingRange([0, 10])}
                size="small"
                sx={{
                  backgroundColor: alpha(theme.palette.primary.main, 0.1),
                  color: theme.palette.primary.main,
                  fontWeight: 500,
                }}
              />
            )}
            {sortBy !== "none" && (
              <Chip
                label={`Sort: ${sortBy.replace("-", " ").replace(/(^\w{1})|(\s+\w{1})/g, (letter) => letter.toUpperCase())}`}
                onDelete={() => setSortBy("none")}
                size="small"
                sx={{
                  backgroundColor: alpha(theme.palette.primary.main, 0.1),
                  color: theme.palette.primary.main,
                  fontWeight: 500,
                }}
              />
            )}
          </Stack>
        </Box>
      )}
    </Box>
  )

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Navbar
        mode={mode}
        toggleTheme={() => setMode((m) => (m === "light" ? "dark" : "light"))}
        onSearch={handleSearch}
        searchQuery={searchQuery}
      />

      <Box
        sx={{
          background:
            theme.palette.mode === "dark"
              ? "linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)"
              : "linear-gradient(135deg, #f5f7fa 0%, #e4e8f0 100%)",
          minHeight: "100vh",
          pt: 2,
          pb: 6,
        }}
      >
        <Container maxWidth="xl">
          <Grid container spacing={3}>
            {!isMobile && (
              <Grid item xs={12} md={3} lg={2.5}>
                <Paper
                  elevation={3}
                  sx={{
                    borderRadius: "16px",
                    overflow: "hidden",
                    height: "fit-content",
                    background: theme.palette.background.paper,
                  }}
                >
                  {filterContent}
                </Paper>
              </Grid>
            )}

            <Grid item xs={12} md={9} lg={9.5}>
              {isMobile && (
                <Button
                  variant="contained"
                  startIcon={<TuneIcon />}
                  onClick={toggleDrawer}
                  fullWidth
                  sx={{
                    mb: 3,
                    borderRadius: "12px",
                    textTransform: "none",
                    fontWeight: "bold",
                    py: 1.2,
                    boxShadow: "0 4px 12px rgba(0,0,0,0.15)",
                  }}
                >
                  Filters & Sorting
                </Button>
              )}

              <Box sx={{ mb: 3, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                <Typography
                  variant="h5"
                  fontWeight="bold"
                  sx={{ color: theme.palette.mode === "dark" ? "white" : "text.primary" }}
                >
                  {filteredMovies.length > 0 ? `Showing ${filteredMovies.length} movies` : "No movies found"}
                </Typography>
              </Box>

              {loading && (
                <Box sx={{ display: "flex", flexDirection: "column", alignItems: "center", my: 8 }}>
                  <CircularProgress size={60} thickness={4} sx={{ color: theme.palette.primary.main }} />
                  <Typography sx={{ mt: 2, fontWeight: "medium" }}>Loading movies...</Typography>
                </Box>
              )}

              {error && !movies.length && (
                <Paper
                  sx={{
                    p: 4,
                    textAlign: "center",
                    borderRadius: "16px",
                    background: alpha(theme.palette.error.main, 0.05),
                    border: `1px solid ${alpha(theme.palette.error.main, 0.2)}`,
                  }}
                  elevation={0}
                >
                  <Typography variant="h6" color="error" fontWeight="bold">
                    {error}
                  </Typography>
                  <Typography variant="body2" color="text.secondary" sx={{ mt: 1 }}>
                    Please try again later or check your connection
                  </Typography>
                </Paper>
              )}

              {!loading && filteredMovies.length === 0 && (
                <Paper
                  sx={{
                    p: 4,
                    textAlign: "center",
                    borderRadius: "16px",
                    background: alpha(theme.palette.info.main, 0.05),
                    border: `1px solid ${alpha(theme.palette.info.main, 0.2)}`,
                  }}
                  elevation={0}
                >
                  <Typography variant="h6" fontWeight="bold">
                    No movies match your filters
                  </Typography>
                  <Typography variant="body2" color="text.secondary" sx={{ mt: 1 }}>
                    Try adjusting your search criteria or clearing some filters
                  </Typography>
                  <Button
                    variant="outlined"
                    color="primary"
                    onClick={clearAllFilters}
                    sx={{ mt: 2, borderRadius: "12px", textTransform: "none", fontWeight: "bold" }}
                  >
                    Clear All Filters
                  </Button>
                </Paper>
              )}

              <Grid container spacing={3}>
                {!loading &&
                  filteredMovies.map((movie) => (
                    <Grid key={movie.id} item xs={12} sm={6} md={4} lg={3} xl={2.4}>
                      <MovieCard movie={movie} />
                    </Grid>
                  ))}
              </Grid>
            </Grid>
          </Grid>
        </Container>
      </Box>

      {isMobile && (
        <Drawer
          anchor="bottom"
          open={drawerOpen}
          onClose={toggleDrawer}
          PaperProps={{
            sx: {
              borderTopLeftRadius: "16px",
              borderTopRightRadius: "16px",
              maxHeight: "90vh",
            },
          }}
        >
          {filterContent}
        </Drawer>
      )}
    </ThemeProvider>
  )
}
