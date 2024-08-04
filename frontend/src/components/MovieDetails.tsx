import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

interface Movie {
    id: number;
    title: string;
    year: string;
    summary: string; 
}

const BASE_URL = 'http://localhost:8000/';


const MovieDetails: React.FC = () => {
    const { id } = useParams<{ id: string }>();
    const [movie, setMovie] = useState<Movie | null>(null);
    const [isAuth, setIsAuth] = useState(false);
    useEffect(() => {
        const checkAuth = () => {
            if (localStorage.getItem('access_token')) {
              setIsAuth(true);
            }
          };
      
          checkAuth();
    }, []);


    useEffect(() => {
        const fetchMovie = async () => {
            try {
                const response = await fetch(`${BASE_URL}/main/movies/${id}`);
                const data: Movie = await response.json();
                setMovie(data);
            } catch (error) {
                console.error(error);
            }
        };

        fetchMovie();
    }, [id]); 

    if (!movie) return <p>No movie found.</p>;

    
    const handleDelete = async () => {
        
        try {
            if(window.confirm('Are you sure you want to delete this movie?')) {
                const token = localStorage.getItem("access_token");
                console.log(token);
                if (!token) {
                    alert('No authentication token found');
                    return;
                }
                await fetch(`${BASE_URL}/main/movies/${id}`, {
                    method: 'DELETE',
                    headers: {
                        'Authorization': `Bearer ${token}`,
                        'Content-Type': 'application/json',
                    },
                    credentials: 'include',
                });
            }
            }
            catch (error) {
                console.error('Error:', error);
            }
        }

    return (
        <div>
            <h2>{movie.title}</h2>
            <p>Year: {movie.year}</p>
            <p>Description: {movie.summary}</p>
            {isAuth && (
        <button onClick={handleDelete}>Delete Movie</button>
      )}
        </div>
    );
};

export default MovieDetails;