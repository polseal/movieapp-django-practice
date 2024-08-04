import { useState } from "react";

const BASE_URL = 'http://localhost:8000/';


const CreateMovie = () => {
    const [title, setName] = useState("");
    const [year, setYear] = useState(0);
    const [summary, setSummary] = useState("");
    const genre = ['4'];
    const [isLoading, setIsLoading] = useState(false); 


    const createMovie = async () => {
        setIsLoading(true); 
        
        try {
            await fetch(`${BASE_URL}/main/movies/create`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${localStorage.getItem('access_token')}`,
                },
                body: JSON.stringify({ title, year, genre, summary }),
            });
        } catch (error) {
            console.error("Error:", error);
        } finally {
            setIsLoading(false); 
        }
    };
    
    return (
        <div>
        <h1>Create Movie</h1>
        <input
            type="text"
            placeholder="Title"
            value={title}
            onChange={(e) => setName(e.target.value)}
        />
        <input
            type="number"
            placeholder="Year"
            value={year}
            onChange={(e) => setYear(parseInt(e.target.value))}
        />
        <input
            type="text"
            placeholder="Summary"
            value={summary}
            onChange={(e) => setSummary(e.target.value)}
        />
        <button onClick={createMovie} disabled={isLoading}>
            {isLoading ? "Loading..." : "Create"}
        </button>
        </div>
    );
}
export default CreateMovie;