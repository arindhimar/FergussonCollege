"use client"
import { Card, CardMedia, CardContent, Typography, CardActions, Button, Box, Chip, Stack } from "@mui/material"
import Link from "next/link"
import { CalendarMonth, Star, AccessTime } from "@mui/icons-material"
import { useTheme, alpha } from "@mui/material/styles"

export default function MovieCard({ movie }) {
  const theme = useTheme()

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
          borderRadius: "16px",
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
          boxShadow: theme.palette.mode === "dark" ? "0 10px 30px rgba(0,0,0,0.7)" : "0 10px 30px rgba(0,0,0,0.15)",
        },
        overflow: "hidden",
        borderRadius: "16px",
        background: theme.palette.background.paper,
      }}
    >
      <Box sx={{ position: "relative", paddingTop: "150%", overflow: "hidden", bgcolor: "grey.900" }}>
        <CardMedia
          component="img"
          image={movie.primaryImage || "/placeholder.svg?height=450&width=300"}
          alt={movie.title || "Movie poster"}
          sx={{
            position: "absolute",
            top: 0,
            left: 0,
            width: "100%",
            height: "100%",
            objectFit: "cover",
            transition: "transform 0.5s",
            "&:hover": {
              transform: "scale(1.05)",
            },
          }}
        />
        <Box
          sx={{
            position: "absolute",
            top: 10,
            right: 10,
            bgcolor: alpha(theme.palette.common.black, 0.7),
            color: "white",
            borderRadius: "12px",
            px: 1,
            py: 0.5,
            display: "flex",
            alignItems: "center",
            gap: 0.5,
            backdropFilter: "blur(4px)",
          }}
        >
          <Star sx={{ fontSize: 16, color: "gold" }} />
          <Typography variant="body2" fontWeight="bold">
            {movie.rating || "N/A"}
          </Typography>
        </Box>
      </Box>

      <CardContent sx={{ flexGrow: 1, p: 2 }}>
        <Typography
          variant="h6"
          gutterBottom
          sx={{
            fontWeight: "bold",
            overflow: "hidden",
            textOverflow: "ellipsis",
            display: "-webkit-box",
            WebkitLineClamp: 1,
            WebkitBoxOrient: "vertical",
            color: theme.palette.mode === "dark" ? "white" : "text.primary",
          }}
          title={movie.title}
        >
          {movie.title || "Unknown Title"}
        </Typography>

        <Stack direction="row" spacing={2} sx={{ mb: 1 }}>
          <Box sx={{ display: "flex", alignItems: "center", gap: 0.5 }}>
            <CalendarMonth sx={{ fontSize: 16, color: theme.palette.primary.main }} />
            <Typography variant="body2" color="text.secondary" fontWeight="medium">
              {movie.year || "N/A"}
            </Typography>
          </Box>

          {movie.duration && (
            <Box sx={{ display: "flex", alignItems: "center", gap: 0.5 }}>
              <AccessTime sx={{ fontSize: 16, color: theme.palette.primary.main }} />
              <Typography variant="body2" color="text.secondary" fontWeight="medium">
                {movie.duration}
              </Typography>
            </Box>
          )}
        </Stack>

        {movie.genres && movie.genres.length > 0 && (
          <Box sx={{ mt: 1, display: "flex", flexWrap: "wrap", gap: 0.5 }}>
            {movie.genres.slice(0, 3).map((genre, index) => (
              <Chip
                key={index}
                label={genre}
                size="small"
                sx={{
                  height: "24px",
                  fontSize: "0.7rem",
                  fontWeight: "medium",
                  bgcolor: alpha(theme.palette.primary.main, 0.1),
                  color: theme.palette.primary.main,
                  borderRadius: "8px",
                }}
              />
            ))}
            {movie.genres.length > 3 && (
              <Chip
                label={`+${movie.genres.length - 3}`}
                size="small"
                sx={{
                  height: "24px",
                  fontSize: "0.7rem",
                  fontWeight: "medium",
                  bgcolor: alpha(theme.palette.primary.main, 0.1),
                  color: theme.palette.primary.main,
                  borderRadius: "8px",
                }}
              />
            )}
          </Box>
        )}
      </CardContent>
        <CardActions sx={{ justifyContent: "center", p: 2, pt: 0 }}>
          <Link href={`/details?id=${movie.id}`} passHref style={{ textDecoration: "none", width: "100%" }}>
            <Button
              size="medium"
              variant="contained"
              fullWidth
              sx={{
                borderRadius: "12px",
                textTransform: "none",
                fontWeight: "bold",
                background: theme.palette.primary.main,
                "&:hover": {
                  background: theme.palette.primary.dark,
                },
                py: 1,
              }}
            >
              View Details
            </Button>
          </Link>
        </CardActions>
      </Card>
  )
}
