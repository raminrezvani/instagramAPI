import React, { useState } from 'react';
import { 
    Button, 
    TextField, 
    Container, 
    Typography, 
    Box,
    Grid 
} from '@mui/material';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom';

const SignIn = () => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        username: '',
        password: '',
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    // In the handleSubmit function:
    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/api/signin/', {
                username: formData.username,
                password: formData.password
            });
            
            // Store the token in localStorage
            localStorage.setItem('token', response.data.token);
            
            console.log('Signin successful:', response.data);
            navigate('/signin-success');  // Redirect to success page
        } catch (error) {
            console.error('Signin error:', error.response?.data || error.message);
            alert(error.response?.data?.error || 'Login failed');
        }
    };

    return (
        <Container component="main" maxWidth="xs">
            <Box sx={{ marginTop: 8, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                <Typography component="h1" variant="h5">
                    Sign In
                </Typography>
                <Box component="form" onSubmit={handleSubmit} sx={{ mt: 3 }}>
                    <Grid container spacing={2}>
                        <Grid item xs={12}>
                            <TextField
                                required
                                fullWidth
                                name="username"
                                label="Username"
                                onChange={handleChange}
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                required
                                fullWidth
                                name="password"
                                label="Password"
                                type="password"
                                onChange={handleChange}
                            />
                        </Grid>
                    </Grid>
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        sx={{ mt: 3, mb: 2 }}
                    >
                        Sign In
                    </Button>
                    <Link to="/signup" style={{ textDecoration: 'none', width: '100%' }}>
                        <Button
                            fullWidth
                            variant="outlined"
                        >
                            Don't have an account? Sign Up
                        </Button>
                    </Link>
                </Box>
            </Box>
        </Container>
    );
};

export default SignIn;