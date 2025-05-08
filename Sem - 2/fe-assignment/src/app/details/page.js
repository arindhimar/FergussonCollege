"use client"
import { useState, useEffect } from "react"
import { useSearchParams } from "next/navigation"
import {
  Typography,
  Button,
  Container,
  Box,
  Paper,
  Grid,
  Chip,
  Rating,
  Divider,
  CircularProgress,
  Stack,
} from "@mui/material"
import Link from "next/link"
import Image from "next/image"
import ArrowBackIcon from "@mui/icons-material/ArrowBack"
import CalendarMonthIcon from "@mui/icons-material/CalendarMonth"
import StarIcon from "@mui/icons-material/Star"
import MovieIcon from "@mui/icons-material/Movie"

export default function DetailsPage() {
  const searchParams = useSearchParams()
  const movieId = searchParams.get("id")
  const [movie, setMovie] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState("")

  useEffect(() => {
    // In a real app, you would fetch the specific movie details using the ID
    // For this example, we'll simulate a movie details fetch
    const fetchMovieDetails = async () => {
      setLoading(true)
      try {
        // This would be a real API call in a production app
        // const response = await axios.get(`/api/movies/${movieId}`)
        // setMovie(response.data)

        // For demo purposes, create a mock movie
        setTimeout(() => {
          const mockMovie = {
            id: movieId,
            title: "The Movie Title",
            year: 2023,
            rating: 7.5,
            poster: "https://via.placeholder.com/500x750?text=Movie+Poster",
            genres: ["Action", "Adventure", "Sci-Fi"],
            description:
              "This is a detailed description of the movie. It contains information about the plot, characters, and other interesting facts about the film. This would typically be a longer paragraph that gives the viewer a good understanding of what the movie is about without spoiling too much of the story.",
            director: "Famous Director",
            cast: ["Actor One", "Actor Two", "Actor Three"],
            runtime: "2h 15m",
            releaseDate: "June 15, 2023",
          }
          setMovie(mockMovie)
          setLoading(false)
        }, 1000)
      } catch (err) {
        console.error("Error fetching movie details:", err)
        setError("Failed to load movie details")
        setLoading(false)
      }
    }

    if (movieId) {
      fetchMovieDetails()
    } else {
      setError("No movie ID provided")
      setLoading(false)
    }
  }, [movieId])

  if (loading) {
    return (
      <Container sx={{ py: 5, textAlign: "center" }}>
        <CircularProgress />
        <Typography sx={{ mt: 2 }}>Loading movie details...</Typography>
      </Container>
    )
  }

  if (error) {
    return (
      <Container sx={{ py: 5 }}>
        <Paper sx={{ p: 4, textAlign: "center" }}>
          <Typography variant="h5" color="error">
            {error}
          </Typography>
          <Link href="/" passHref>
            <Button startIcon={<ArrowBackIcon />} sx={{ mt: 2 }}>
              Back to Movies
            </Button>
          </Link>
        </Paper>
      </Container>
    )
  }

  if (!movie) {
    return (
      <Container sx={{ py: 5 }}>
        <Paper sx={{ p: 4, textAlign: "center" }}>
          <Typography variant="h5">Movie not found</Typography>
          <Link href="/" passHref>
            <Button startIcon={<ArrowBackIcon />} sx={{ mt: 2 }}>
              Back to Movies
            </Button>
          </Link>
        </Paper>
      </Container>
    )
  }

  return (
    <Container sx={{ py: 5 }}>
      <Link href="/" passHref>
        <Button startIcon={<ArrowBackIcon />} sx={{ mb: 3 }}>
          Back to Movies
        </Button>
      </Link>

      <Paper sx={{ p: 4 }}>
        <Grid container spacing={4}>
          {/* Movie Poster */}
          <Grid item xs={12} md={4}>
            <Box
              sx={{
                position: "relative",
                height: { xs: "400px", md: "500px" },
                width: "100%",
                borderRadius: 2,
                overflow: "hidden",
                boxShadow: 3,
              }}
            >
              <Image src={movie.poster || "/placeholder.svg"} alt={movie.title} fill style={{ objectFit: "cover" }} />
            </Box>
          </Grid>

          {/* Movie Details */}
          <Grid item xs={12} md={8}>
            <Typography variant="h4" gutterBottom>
              {movie.title}
            </Typography>

            <Stack direction="row" spacing={2} sx={{ mb: 2, flexWrap: "wrap", gap: 1 }}>
              {movie.genres.map((genre, index) => (
                <Chip key={index} label={genre} color="primary" variant="outlined" />
              ))}
            </Stack>

            <Stack direction="row" spacing={3} sx={{ mb: 3 }}>
              <Box sx={{ display: "flex", alignItems: "center" }}>
                <CalendarMonthIcon sx={{ mr: 1 }} />
                <Typography>{movie.year}</Typography>
              </Box>

              <Box sx={{ display: "flex", alignItems: "center" }}>
                <StarIcon sx={{ mr: 1, color: "gold" }} />
                <Typography>{movie.rating}/10</Typography>
              </Box>

              <Box sx={{ display: "flex", alignItems: "center" }}>
                <MovieIcon sx={{ mr: 1 }} />
                <Typography>{movie.runtime}</Typography>
              </Box>
            </Stack>

            <Divider sx={{ my: 2 }} />

            <Typography variant="h6" gutterBottom>
              Overview
            </Typography>
            <Typography paragraph>{movie.description}</Typography>

            <Divider sx={{ my: 2 }} />

            <Grid container spacing={2}>
              <Grid item xs={12} sm={6}>
                <Typography variant="subtitle1" fontWeight="bold">
                  Director
                </Typography>
                <Typography paragraph>{movie.director}</Typography>
              </Grid>

              <Grid item xs={12} sm={6}>
                <Typography variant="subtitle1" fontWeight="bold">
                  Release Date
                </Typography>
                <Typography paragraph>{movie.releaseDate}</Typography>
              </Grid>

              <Grid item xs={12}>
                <Typography variant="subtitle1" fontWeight="bold">
                  Cast
                </Typography>
                <Typography paragraph>{movie.cast.join(", ")}</Typography>
              </Grid>
            </Grid>

            <Box sx={{ mt: 3, display: "flex", justifyContent: "center" }}>
              <Rating
                value={movie.rating / 2} // Convert from 10-scale to 5-scale
                precision={0.5}
                readOnly
                size="large"
              />
            </Box>
          </Grid>
        </Grid>
      </Paper>
    </Container>
  )
}
