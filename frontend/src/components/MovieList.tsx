import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';
import './App.css';

interface Movie {
    id: number;
    title: string;
    year: number;
}


const BASE_URL = 'http://localhost:8000/';

const MovieList: React.FC = () => {
    const [movies, setMovies] = React.useState<Movie[]>([]);
    useEffect(() => {

        const fetchAllMovies = async () => {
            try {
                const response = await fetch(`${BASE_URL}main/movies`);
                const data: Movie[] = await response.json();
                setMovies(data);
            }
            catch (error) {
                console.error(error);
            }
        }
        fetchAllMovies();
    }, []);

    return (
            <div className="Movielist-container">
                <div className="Movielist-form-content">
                <h3 className="Movielist-form-title">Movie List</h3>
            <ul>
                {movies.map((movie) => (
                    <li key={movie.id}>
                    <Link to={`/movies/${movie.id}`}>
                        {movie.title} - {movie.year}
                    </Link>
                </li>
                ))}
            </ul>
            </div>
            </div>
    );
};

export default MovieList;