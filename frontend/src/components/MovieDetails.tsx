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

    return (
        <div>
            <h2>{movie.title}</h2>
            <p>Year: {movie.year}</p>
            <p>Description: {movie.summary}</p>
        </div>
    );
};

export default MovieDetails;