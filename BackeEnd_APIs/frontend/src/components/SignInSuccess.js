import React from 'react';
import { Container, Typography, Box, Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';

const SignInSuccess = () => {
    const navigate = useNavigate();

    return (
        <Container component="main" maxWidth="xs">
            <Box
                sx={{
                    marginTop: 8,
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                }}
            >
                <Typography component="h1" variant="h4" sx={{ mb: 4 }}>
                    Welcome Back! 🎉
                </Typography>
                <Typography variant="h6" sx={{ mb: 3 }}>
                    You have successfully signed in
                </Typography>
                <Button
                    variant="contained"
                    onClick={() => navigate('/')}
                    sx={{ mt: 3 }}
                >
                    Go to Home
                </Button>
            </Box>
        </Container>
    );
};

export default SignInSuccess;