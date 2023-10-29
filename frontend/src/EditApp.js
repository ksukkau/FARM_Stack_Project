import React, {useState, useEffect} from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'

export default function App() {

  const [pokemons, setPokemons] = useState([])
  const [currentPage, setCurrentPage] = useState(1);
  const [pokemonsPerPage] = useState(10);

  let firstload = true;
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/v1/allpokemon')
      .then(res => res.data)
      .then(res => {
        if(firstload){
          firstload = false
          setPokemons(res)
        }
      })
      .catch(err => console.log("err", err))
  }, [])
  return (
    <div className="App">
      Hello World
    </div>
  );
}
