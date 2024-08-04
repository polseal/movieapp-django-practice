
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import MovieList from './MovieList';
import MovieDetails from './MovieDetails';
import Navigator from './Navigator';

function App() {

  return (
    <Router>
      <Navigation></Navigation>
    <Routes>
      <Route path="/" element={<MovieList/>} />
      <Route path="/movies/:id" element={<MovieDetails />} />
    </Routes>
  </Router>
  );
}

export default App;
