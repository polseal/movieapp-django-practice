
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import MovieList from './MovieList';
import MovieDetails from './MovieDetails';
import Navigator from './Navigator';
import Login  from './Login';
import Logout from './Logout';
import CreateMovie from './CreateMovie';


function App() {

  return (
    <Router>
      <Navigator />
    <Routes>
      <Route path="/" element={<MovieList/>} />
      <Route path="/movies/:id" element={<MovieDetails />} />
      <Route path="/movies/create" element={<CreateMovie />} />
      <Route path="/login" element={<Login/>}/>
      <Route path="/logout" element={<Logout/>}/>
    </Routes>
  </Router>
  );
}

export default App;
