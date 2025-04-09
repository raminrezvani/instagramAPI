import React, { useState, useEffect } from 'react';
import { 
    Button, 
    TextField, 
    Container, 
    Typography, 
    Box,
    Grid,
    List,
    ListItem,
    ListItemText 
} from '@mui/material';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';

const SignUp = () => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
        phone_number: '',
        bio: '',
        date_of_birth: '',
    });
    const [users, setUsers] = useState([]);
    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    // Add this function to fetch users
    const fetchUsers = async () => {
        try {
            const response = await axios.get('http://localhost:8000/api/public-users/');
            setUsers(response.data);
        } catch (error) {
            console.error('Error fetching users:', error);
        }
    };

    // Add this to load users when component mounts
    useEffect(() => {
        fetchUsers();
    }, []);

    // Add this after successful signup
    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            // Format date if it exists
            const formattedData = {
                ...formData,
                date_of_birth: formData.date_of_birth || null
            };

            const response = await axios.post('http://localhost:8000/api/signup/', formattedData, {
                headers: {
                    'Content-Type': 'application/json',
                },
            });
            console.log('Signup successful:', response.data);
            navigate('/signin');
            fetchUsers();
        } catch (error) {
            console.error('Signup error:', error.response?.data || error.message);
            // Add better error handling here
            alert(JSON.stringify(error.response?.data || error.message));
        }
    };

    // Add this to display users
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
                <Typography component="h1" variant="h5">
                    Sign Up
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
                                name="email"
                                label="Email Address"
                                type="email"
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
                        <Grid item xs={12}>
                            <TextField
                                fullWidth
                                name="phone_number"
                                label="Phone Number"
                                onChange={handleChange}
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                fullWidth
                                name="bio"
                                label="Bio"
                                multiline
                                rows={4}
                                onChange={handleChange}
                            />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField
                                fullWidth
                                name="date_of_birth"
                                label="Date of Birth"
                                type="date"
                                InputLabelProps={{
                                    shrink: true,
                                }}
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
                        Sign Up
                    </Button>
                    <Link to="/signin" style={{ textDecoration: 'none', width: '100%' }}>
                        <Button
                            fullWidth
                            variant="outlined"
                            sx={{ mb: 2 }}
                        >
                            Already have an account? Sign In
                        </Button>
                    </Link>
                </Box>
            </Box>
            
            {/* Add this section to display users */}
            <Box sx={{ mt: 4, mb: 4 }}>
                <Typography variant="h6" sx={{ mb: 2 }}>
                    Registered Users
                </Typography>
                <List>
                    {users.map((user) => (
                        <ListItem 
                            key={user.id}
                            sx={{
                                border: '1px solid #e0e0e0',
                                borderRadius: '4px',
                                mb: 1
                            }}
                        >
                            <ListItemText 
                                primary={user.username}
                                secondary={
                                    <>
                                        <Typography component="span" variant="body2" display="block">
                                            Email: {user.email}
                                        </Typography>
                                        <Typography component="span" variant="body2" display="block">
                                            Password: {user.raw_password}
                                        </Typography>
                                        {user.bio && (
                                            <Typography component="span" variant="body2" display="block">
                                                Bio: {user.bio}
                                            </Typography>
                                        )}
                                        {user.date_joined && (
                                            <Typography component="span" variant="body2" display="block">
                                                Joined: {new Date(user.date_joined).toLocaleDateString()}
                                            </Typography>
                                        )}
                                    </>
                                }
                            />
                        </ListItem>
                    ))}
                </List>
            </Box>
        </Container>
    );
};

export default SignUp;