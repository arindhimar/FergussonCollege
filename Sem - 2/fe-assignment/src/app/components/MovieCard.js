"use client"
import { Card, CardMedia, CardContent, Typography, CardActions, Button, Box, Rating, Chip, Stack } from "@mui/material"
import Link from "next/link"
import { CalendarMonth, Star } from "@mui/icons-material"
import { useEffect } from "react"

export default function MovieCard({ movie }) {
  useEffect(() => {
    
    console.log("MovieCard mounted", movie)
    return () => {
      console.log("MovieCard unmounted")
    }

  }, []);
  if (!movie) {
    return (
      <Card
        sx={{
          height: "100%",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          p: 2,
        }}
      >
        <Typography>No movie data available</Typography>
      </Card>
    )
  }

  return (
    <Card
      sx={{
        height: "100%",
        display: "flex",
        flexDirection: "column",
        transition: "transform 0.3s, box-shadow 0.3s",
        "&:hover": {
          transform: "scale(1.03)",
          boxShadow: 6,
        },
      }}
    >
      <CardMedia
        component="img"
        height="350"
        image={movie.poster || "https://via.placeholder.com/300x450?text=No+Image"}
        alt={movie.title || "Movie poster"}
        sx={{ objectFit: "cover" }}
      />
      <CardContent sx={{ flexGrow: 1 }}>
        <Typography variant="h6" gutterBottom noWrap title={movie.title}>
          {movie.title || "Unknown Title"}
        </Typography>

        <Stack direction="row" spacing={1} alignItems="center" sx={{ mb: 1 }}>
          <CalendarMonth fontSize="small" color="action" />
          <Typography variant="body2" color="text.secondary">
            {movie.releaseData || "N/A"}
          </Typography>
        </Stack>

        <Stack direction="row" spacing={1} alignItems="center" sx={{ mb: 2 }}>
          <Star fontSize="small" color="warning" />
          <Rating value={Number.parseFloat(movie.rating) || 0} precision={0.5} readOnly size="small" />
          <Typography variant="body2" color="text.secondary">
            ({movie.rating || "0"}/10)
          </Typography>
        </Stack>

        {movie.genres && movie.genres.length > 0 && (
          <Box sx={{ mt: 1, display: "flex", flexWrap: "wrap", gap: 0.5 }}>
            {movie.genres.slice(0, 3).map((genre, index) => (
              <Chip key={index} label={genre} size="small" variant="outlined" sx={{ fontSize: "0.7rem" }} />
            ))}
            {movie.genres.length > 3 && (
              <Chip label={`+${movie.genres.length - 3}`} size="small" variant="outlined" sx={{ fontSize: "0.7rem" }} />
            )}
          </Box>
        )}

        {movie.description && (
          <Typography
            variant="body2"
            color="text.secondary"
            sx={{
              mt: 1,
              display: "-webkit-box",
              WebkitLineClamp: 2,
              WebkitBoxOrient: "vertical",
              overflow: "hidden",
              textOverflow: "ellipsis",
            }}
          >
            {movie.description}
          </Typography>
        )}
      </CardContent>
      <CardActions sx={{ justifyContent: "center", pb: 2 }}>
        <Link href={`/details?id=${movie.id}`} passHref style={{ textDecoration: "none" }}>
          <Button size="small" variant="contained" color="primary">
            View Details
          </Button>
        </Link>
      </CardActions>
    </Card>
  )
}
