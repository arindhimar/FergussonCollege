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
  InputLabel,
  Select,
  MenuItem,
  TextField,
  Slider,
  Chip,
  Paper,
  Stack,
  Divider,
  InputAdornment,
} from "@mui/material"
import { getTheme } from "../theme/theme"
import Navbar from "../components/Navbar"
import MovieCard from "../components/MovieCard"
import SearchIcon from "@mui/icons-material/Search"
import SortIcon from "@mui/icons-material/Sort"
import FilterListIcon from "@mui/icons-material/FilterList"

// Sample genres for the filter
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

  // Filter and sort states
  const [searchQuery, setSearchQuery] = useState("")
  const [selectedGenres, setSelectedGenres] = useState([])
  const [ratingRange, setRatingRange] = useState([0, 10])
  const [sortBy, setSortBy] = useState("none")

  // Processed movies after filtering and sorting
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
        console.log("ARRAY LENGTH:", arr.length, "FIRST ITEM:", arr[0])

        // Transform the data to match our MovieCard component expectations
        const transformedMovies = arr.map((movie) => ({
          id: movie.id || `movie-${Math.random()}`,
          title: movie.primaryTitle || "Unknown Title",
          year: movie.startYear || "N/A",
          rating: movie.averageRating || 0,
          poster: movie.primaryImage || "https://via.placeholder.com/300x450?text=No+Image",
          genres: movie.genres || ["Unknown"],
          description: movie.description || "No description available",
        }))

        setMovies(transformedMovies)
        setFilteredMovies(transformedMovies)
      } catch (e) {
        console.error(e)
        setError("Could not load movies")

        // For development purposes, create some sample data if the API fails
        const sampleMovies = Array(12)
          .fill(0)
          .map((_, i) => ({
            id: `sample-${i}`,
            title: `Sample Movie ${i + 1}`,
            year: 2000 + Math.floor(Math.random() * 23),
            rating: (Math.random() * 10).toFixed(1),
            poster: "https://via.placeholder.com/300x450?text=Sample+Movie",
            genres: [GENRES[Math.floor(Math.random() * GENRES.length)]],
            description: "This is a sample movie description.",
          }))

        setMovies(sampleMovies)
        setFilteredMovies(sampleMovies)
      } finally {
        setLoading(false)
      }
    }
    fetchMovies()
  }, [])

  // Apply filters and sorting whenever the filter criteria change
  useEffect(() => {
    let result = [...movies]

    // Apply search filter
    if (searchQuery) {
      const query = searchQuery.toLowerCase()
      result = result.filter(
        (movie) => movie.title.toLowerCase().includes(query) || movie.description.toLowerCase().includes(query),
      )
    }

    // Apply genre filter
    if (selectedGenres.length > 0) {
      result = result.filter((movie) => movie.genres && selectedGenres.some((genre) => movie.genres.includes(genre)))
    }

    // Apply rating filter
    result = result.filter((movie) => movie.rating >= ratingRange[0] && movie.rating <= ratingRange[1])

    // Apply sorting
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
        // No sorting
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
          py: 5,
          px: 2,
          background:
            mode === "light"
              ? "linear-gradient(to right, #e0eafc, #cfdef3)"
              : "linear-gradient(to right, #1e1e1e, #121212)",
          minHeight: "100vh",
        }}
      >
        <Container>
          {/* Filters and Sorting Section */}
          <Paper sx={{ p: 3, mb: 4 }}>
            <Typography variant="h6" gutterBottom>
              <FilterListIcon sx={{ mr: 1, verticalAlign: "middle" }} />
              Filters & Sorting
            </Typography>

            <Grid container spacing={3}>
              {/* Search */}
              <Grid item xs={12} md={4}>
                <TextField
                  fullWidth
                  label="Search Movies"
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
                />
              </Grid>

              {/* Genre Filter */}
              <Grid item xs={12} md={4}>
                <FormControl fullWidth>
                  <InputLabel id="genre-select-label">Genre</InputLabel>
                  <Select
                    labelId="genre-select-label"
                    id="genre-select"
                    multiple
                    value={selectedGenres}
                    onChange={handleGenreChange}
                    renderValue={(selected) => (
                      <Box sx={{ display: "flex", flexWrap: "wrap", gap: 0.5 }}>
                        {selected.map((value) => (
                          <Chip
                            key={value}
                            label={value}
                            onDelete={() => handleGenreDelete(value)}
                            onMouseDown={(event) => {
                              event.stopPropagation()
                            }}
                          />
                        ))}
                      </Box>
                    )}
                  >
                    {GENRES.map((genre) => (
                      <MenuItem key={genre} value={genre}>
                        {genre}
                      </MenuItem>
                    ))}
                  </Select>
                </FormControl>
              </Grid>

              {/* Sort Options */}
              <Grid item xs={12} md={4}>
                <FormControl fullWidth>
                  <InputLabel id="sort-select-label">Sort By</InputLabel>
                  <Select
                    labelId="sort-select-label"
                    id="sort-select"
                    value={sortBy}
                    onChange={handleSortChange}
                    startAdornment={
                      <InputAdornment position="start">
                        <SortIcon />
                      </InputAdornment>
                    }
                  >
                    <MenuItem value="none">None</MenuItem>
                    <MenuItem value="title-asc">Title (A-Z)</MenuItem>
                    <MenuItem value="title-desc">Title (Z-A)</MenuItem>
                    <MenuItem value="year-asc">Year (Oldest First)</MenuItem>
                    <MenuItem value="year-desc">Year (Newest First)</MenuItem>
                    <MenuItem value="rating-asc">Rating (Low to High)</MenuItem>
                    <MenuItem value="rating-desc">Rating (High to Low)</MenuItem>
                  </Select>
                </FormControl>
              </Grid>

              {/* Rating Slider */}
              <Grid item xs={12}>
                <Typography id="rating-slider" gutterBottom>
                  Rating Range: {ratingRange[0]} - {ratingRange[1]}
                </Typography>
                <Slider
                  value={ratingRange}
                  onChange={handleRatingChange}
                  valueLabelDisplay="auto"
                  min={0}
                  max={10}
                  step={0.5}
                  marks={[
                    { value: 0, label: "0" },
                    { value: 2.5, label: "2.5" },
                    { value: 5, label: "5" },
                    { value: 7.5, label: "7.5" },
                    { value: 10, label: "10" },
                  ]}
                />
              </Grid>
            </Grid>

            {/* Active Filters Display */}
            {(selectedGenres.length > 0 ||
              searchQuery ||
              ratingRange[0] > 0 ||
              ratingRange[1] < 10 ||
              sortBy !== "none") && (
              <Box sx={{ mt: 2 }}>
                <Divider sx={{ my: 1 }} />
                <Typography variant="body2" color="text.secondary">
                  Active filters:
                </Typography>
                <Stack direction="row" spacing={1} sx={{ mt: 1, flexWrap: "wrap", gap: 1 }}>
                  {searchQuery && (
                    <Chip label={`Search: ${searchQuery}`} onDelete={() => setSearchQuery("")} size="small" />
                  )}
                  {selectedGenres.map((genre) => (
                    <Chip
                      key={genre}
                      label={`Genre: ${genre}`}
                      onDelete={() => handleGenreDelete(genre)}
                      size="small"
                    />
                  ))}
                  {(ratingRange[0] > 0 || ratingRange[1] < 10) && (
                    <Chip
                      label={`Rating: ${ratingRange[0]} - ${ratingRange[1]}`}
                      onDelete={() => setRatingRange([0, 10])}
                      size="small"
                    />
                  )}
                  {sortBy !== "none" && (
                    <Chip
                      label={`Sort: ${sortBy.replace("-", " ").replace(/(^\w{1})|(\s+\w{1})/g, (letter) => letter.toUpperCase())}`}
                      onDelete={() => setSortBy("none")}
                      size="small"
                    />
                  )}
                </Stack>
              </Box>
            )}
          </Paper>

          {/* Results Count */}
          <Typography variant="subtitle1" sx={{ mb: 2 }}>
            Showing {filteredMovies.length} of {movies.length} movies
          </Typography>

          {loading && <CircularProgress sx={{ display: "block", mx: "auto", my: 4 }} />}

          {error && !movies.length && (
            <Typography color="error" align="center" sx={{ my: 4 }}>
              {error}
            </Typography>
          )}

          {/* No Results Message */}
          {!loading && filteredMovies.length === 0 && (
            <Paper sx={{ p: 4, textAlign: "center" }}>
              <Typography variant="h6">No movies match your filters</Typography>
              <Typography variant="body2" color="text.secondary" sx={{ mt: 1 }}>
                Try adjusting your search criteria or clearing some filters
              </Typography>
            </Paper>
          )}

          {/* Movie Grid */}
          <Grid container spacing={3}>
            {!loading &&
              filteredMovies.map((movie) => (
                <Grid key={movie.id} item xs={12} sm={6} md={4} lg={3}>
                  <MovieCard movie={movie} />
                </Grid>
              ))}
          </Grid>
        </Container>
      </Box>
    </ThemeProvider>
  )
}
