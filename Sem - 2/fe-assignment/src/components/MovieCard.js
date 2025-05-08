'use client';
import { Card, CardMedia, CardContent, Typography, CardActions, Button, Box, Rating } from '@mui/material';
import Link from 'next/link';

export default function MovieCard({ movie }) {
  return (
    <Card
      sx={{
        transition: 'transform 0.3s, box-shadow 0.3s',
        '&:hover': {
          transform: 'scale(1.03)',
          boxShadow: 6,
        },
      }}
    >
      <CardMedia component="img" height="350" image={movie.poster} alt={movie.title} />
      <CardContent>
        <Typography variant="h6">{movie.title}</Typography>
        <Typography variant="body2" color="text.secondary">
          Year: {movie.year}
        </Typography>
        <Box sx={{ mt: 1 }}>
          <Rating value={movie.rating} precision={0.5} readOnly />
        </Box>
      </CardContent>
      <CardActions>
        <Link href={`/details?id=${movie.id}`} passHref>
          <Button size="small" variant="contained">View Details</Button>
        </Link>
      </CardActions>
    </Card>
  );
}
