import React from 'react';
import { Container, Typography, Box } from '@mui/material';

const Home = () => {
    return (
        <Container>
            <Box sx={{ mt: 4, textAlign: 'center' }}>
                <Typography variant="h4">Welcome to Home Page</Typography>
                <Typography variant="body1">You have successfully logged in!</Typography>
            </Box>
        </Container>
    );
};

export default Home;