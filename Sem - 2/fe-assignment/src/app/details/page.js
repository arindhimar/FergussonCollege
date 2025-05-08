'use client';

import { useState, useEffect } from 'react';
import { useSearchParams } from 'next/navigation';
import axios from 'axios';
import {
  Typography,
  Button,
  Container,
  Box,
  Paper,
  Grid,
  Chip,
  Divider,
  CircularProgress,
  Stack,
  useTheme,
  useMediaQuery,
  alpha,
  IconButton,
} from '@mui/material';
import Link from 'next/link';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import CalendarMonthIcon from '@mui/icons-material/CalendarMonth';
import StarIcon from '@mui/icons-material/Star';
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import LocalMoviesIcon from '@mui/icons-material/LocalMovies';
import BookmarkBorderIcon from '@mui/icons-material/BookmarkBorder';
import ShareIcon from '@mui/icons-material/Share';

export default function DetailsPage() {
  const searchParams = useSearchParams();
  const movieId = searchParams.get('id');
  const [movie, setMovie] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const theme = useTheme();
  const isMobile = useMediaQuery(theme.breakpoints.down('sm'));

  useEffect(() => {
    if (!movieId) {
      setError('No movie ID provided');
      setLoading(false);
      return;
    }
    (async () => {
      setLoading(true);
      try {
        const res = await axios.get(
          `https://imdb236.p.rapidapi.com/imdb/${movieId}`,
          {
            headers: {
              'x-rapidapi-key': '0cc3d8c429msh967ab5a4fb0a39ep1ec8d4jsnd29731211186',
              'x-rapidapi-host': 'imdb236.p.rapidapi.com',
            },
          }
        );
        setMovie(res.data);
        console.log(res.data.budget);
      } catch (e) {
        console.error(e);
        setError('Failed to load movie details');
      } finally {
        setLoading(false);
      }
    })();
  }, [movieId]);

  if (loading) {
    return (
      <Box
        sx={{
          height: '100vh',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          background:
            theme.palette.mode === 'dark'
              ? 'linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)'
              : 'linear-gradient(135deg, #f5f7fa 0%, #e4e8f0 100%)',
        }}
      >
        <CircularProgress size={60} thickness={4} sx={{ color: theme.palette.primary.main }} />
        <Typography sx={{ mt: 2, fontWeight: 'medium' }}>Loading movie details...</Typography>
      </Box>
    );
  }

  if (error) {
    return (
      <Container sx={{ py: 5 }}>
        <Paper
          sx={{
            p: 4,
            textAlign: 'center',
            borderRadius: '16px',
            background: alpha(theme.palette.error.main, 0.05),
            border: `1px solid ${alpha(theme.palette.error.main, 0.2)}`,
          }}
          elevation={0}
        >
          <Typography variant="h5" color="error" fontWeight="bold">
            {error}
          </Typography>
          <Link href="/" passHref>
            <Button
              startIcon={<ArrowBackIcon />}
              sx={{ mt: 2, borderRadius: '12px', textTransform: 'none', fontWeight: 'bold' }}
              variant="contained"
            >
              Back to Movies
            </Button>
          </Link>
        </Paper>
      </Container>
    );
  }

  if (!movie) return null;

  return (
    <Box
      sx={{
        minHeight: '100vh',
        background:
          theme.palette.mode === 'dark'
            ? 'linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)'
            : 'linear-gradient(135deg, #f5f7fa 0%, #e4e8f0 100%)',
        pb: 6,
      }}
    >
      <Box
        sx={{
          position: 'relative',
          height: { xs: '80px', sm: '80px', md: '100px' },
          backgroundImage: `linear-gradient(to bottom, rgba(0,0,0,0.1), ${theme.palette.mode === 'dark' ? 'rgba(26,26,46,0.95)' : 'rgba(245,247,250,0.95)'
            })`,
          display: 'flex',
          alignItems: 'flex-end',
          mb: { xs: 4, sm: 6, md: 8 },
        }}
      >
        <Link href="/" passHref>
          <Button
            startIcon={<ArrowBackIcon />}
            sx={{
              m: 2,
              borderRadius: '12px',
              textTransform: 'none',
              fontWeight: 'bold',
              bgcolor: alpha(theme.palette.background.paper, 0.8),
              backdropFilter: 'blur(10px)',
              color: theme.palette.text.primary,
              '&:hover': { bgcolor: alpha(theme.palette.background.paper, 0.9) },
            }}
            variant="text"
          >
            Back to Movies
          </Button>
        </Link>
      </Box>

      {/* details panel immediately below */}
      <Container maxWidth="lg" sx={{ mt: 0 }}>
        <Grid container spacing={4}>
          {/* poster & actions */}
          <Grid item xs={12} sm={4} md={3}>
            <Box
              sx={{
                position: 'relative',
                width: '100%',
                pt: '150%',
                borderRadius: '16px',
                overflow: 'hidden',
                boxShadow: '0 10px 30px rgba(0,0,0,0.3)',
              }}
            >
              <Box
                component="img"
                src={movie.primaryImage}
                alt={movie.primaryTitle}
                sx={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', objectFit: 'cover' }}
              />
            </Box>
            <Stack direction="row" spacing={1} sx={{ mt: 2, justifyContent: 'center' }}>
              <IconButton sx={{ bgcolor: alpha(theme.palette.background.paper, 0.8) }}>
                <BookmarkBorderIcon />
              </IconButton>
              <IconButton sx={{ bgcolor: alpha(theme.palette.background.paper, 0.8) }}>
                <ShareIcon />
              </IconButton>
            </Stack>
          </Grid>

          {/* info panel */}
          <Grid item xs={12} sm={8} md={9}>
            <Paper
              elevation={0}
              sx={{
                p: { xs: 3, md: 4 },
                borderRadius: '16px',
                background: alpha(theme.palette.background.paper, 0.8),
                backdropFilter: 'blur(10px)',
              }}
            >
              {/* title */}
              <Typography variant={isMobile ? 'h4' : 'h3'} fontWeight="bold" sx={{ mb: 2 }}>
                {movie.primaryTitle}
              </Typography>

              {/* genres */}
              <Stack direction="row" spacing={1} sx={{ mb: 3, flexWrap: 'wrap', gap: 1 }}>
                {movie.genres.map((g, i) => (
                  <Chip key={i} label={g} sx={{ bgcolor: alpha(theme.palette.primary.main, 0.1), color: theme.palette.primary.main }} />
                ))}
              </Stack>

              {/* meta info */}
              <Grid container spacing={3} sx={{ mb: 3 }}>
                <Grid item xs={6} sm={4}>
                  <Box sx={{ display: 'flex', alignItems: 'center' }}>
                    <StarIcon sx={{ mr: 1, color: 'gold' }} />
                    <Box>
                      <Typography variant="h6" fontWeight="bold">
                        {movie.averageRating}/10
                      </Typography>
                      <Typography variant="body2" color="text.secondary">
                        Rating
                      </Typography>
                    </Box>
                  </Box>
                </Grid>
                <Grid item xs={6} sm={4}>
                  <Box sx={{ display: 'flex', alignItems: 'center' }}>
                    <CalendarMonthIcon sx={{ mr: 1, color: theme.palette.primary.main }} />
                    <Box>
                      <Typography variant="h6" fontWeight="bold">
                        {movie.startYear}
                      </Typography>
                      <Typography variant="body2" color="text.secondary">
                        Year
                      </Typography>
                    </Box>
                  </Box>
                </Grid>
                {movie.runtimeMinutes && (
                  <Grid item xs={6} sm={4}>
                    <Box sx={{ display: 'flex', alignItems: 'center' }}>
                      <AccessTimeIcon sx={{ mr: 1, color: theme.palette.primary.main }} />
                      <Box>
                        <Typography variant="h6" fontWeight="bold">
                          {movie.runtimeMinutes} min
                        </Typography>
                        <Typography variant="body2" color="text.secondary">
                          Duration
                        </Typography>
                      </Box>
                    </Box>
                  </Grid>
                )}
              </Grid>

              <Divider sx={{ my: 3 }} />

              {/* overview */}
              <Typography variant="h5" gutterBottom fontWeight="bold" color={theme.palette.primary.main}>
                Overview
              </Typography>
              <Typography variant="body1" paragraph>
                {movie.description}
              </Typography>

              {/* additional details */}
              <Grid container spacing={3}>
                <Grid item xs={12} sm={6} md={4}>
                  <Typography variant="subtitle1" fontWeight="bold" color={theme.palette.primary.main}>
                    Director
                  </Typography>
                  <Typography>{movie.directors?.map(d => d.fullName).join(', ')}</Typography>
                </Grid>
                <Grid item xs={12} sm={6} md={4}>
                  <Typography variant="subtitle1" fontWeight="bold" color={theme.palette.primary.main}>
                    Budget
                  </Typography>
                  <Typography>
                    {movie.budget ? `$${movie.budget}` : 'N/A'}
                  </Typography>
                </Grid>
                <Grid item xs={12} sm={6} md={4}>
                  <Typography variant="subtitle1" fontWeight="bold" color={theme.palette.primary.main}>
                    Country
                  </Typography>
                  <Typography>{movie.countriesOfOrigin.join(', ')}</Typography>
                </Grid>
              </Grid>
            </Paper>
          </Grid>
        </Grid>
      </Container>
    </Box>
  );
}
