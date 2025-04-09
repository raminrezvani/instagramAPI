import React from 'react';
import { Container, Typography, Box } from '@mui/material';

const Dashboard = () => {
    return (
        <Container>
            <Box sx={{ mt: 4 }}>
                <Typography variant="h4">Welcome to Dashboard</Typography>
                <Typography variant="body1">You are successfully logged in!</Typography>
            </Box>
        </Container>
    );
};

export default Dashboard;