import './css/SearchApp.css';
import React, {useState, useEffect, useContext} from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'
import Pagination from './Pagination';
import Pokemon from './Pokemon'
import SearchInput from './SearchInput'
import { SharedStateContext } from './SharedStateContext';
import Card from 'react-bootstrap/Card';

URL = 'https://farm-stack-project.customcloud.ca'

const filterPokemon = (pokemons, searchInputs) => {
  console.log("entered filter")
  if(searchInputs.name === '' && searchInputs.type.length === 0){
    return pokemons.filter(pokemon =>{
      return ( Number(pokemon.base.HP) <= searchInputs.hp && Number(pokemon.base.Attack) <= searchInputs.attack)})
 } 
  if(searchInputs.name !== '' && searchInputs.type.length === 0){
    console.log("search by name")
    return pokemons.filter(pokemon =>{
      return (
        pokemon.name.english.toLowerCase().includes(searchInputs.name.toLowerCase()) && Number(pokemon.base.HP) <= searchInputs.hp && Number(pokemon.base.Attack) <= searchInputs.attack
      )
    })
  }
  if(searchInputs.name === '' && searchInputs.type.length !== 0){
    return pokemons.filter(pokemon =>{
      return (
        searchInputs.type.every(elem => pokemon.type.includes(elem))&& Number(pokemon.base.HP) <= searchInputs.hp && Number(pokemon.base.Attack) <= searchInputs.attack
      )
    })
  }
  return pokemons.filter(pokemon =>{
    return (
      pokemon.name.english.toLowerCase().includes(searchInputs.name.toLowerCase()) && searchInputs.type.every(elem => pokemon.type.includes(elem)) && Number(pokemon.base.HP) <= searchInputs.hp && Number(pokemon.base.Attack) <= searchInputs.attack
    )
  })
}

export default function App() {

  const [searchInputs, setSearchInputs] = useState({
    name:'',
    type: [],
    hp: 255,
    attack: 255
  })
  const [currentPage, setCurrentPage] = useState(1);
  const [pokemonsPerPage] = useState(10);

  const {pokemons, setPokemons} = useContext(SharedStateContext);

  let firstload = true;
  useEffect(() => {
    axios.get(`${URL}/api/v1/allpokemon`)
      .then(res => res.data)
      .then(res => {
        if(firstload){
          firstload = false
          setPokemons(res)
        }
      })
      .catch(err => console.log("err", err))
  }, [])

  const filteredPokemons = filterPokemon(pokemons, searchInputs)
  
  const indexOfLastRecord = currentPage * pokemonsPerPage;
  const indexOfFirstRecord = indexOfLastRecord - pokemonsPerPage;
  const currentPokemons = filteredPokemons.slice(indexOfFirstRecord, indexOfLastRecord)
  const numberOfPages = Math.ceil(filteredPokemons.length / pokemonsPerPage);

  if(numberOfPages>0){

    if(currentPage > numberOfPages){
      setCurrentPage(1)
      console.log("Changing" + currentPage)
    }
  }


  return (
    <div className="App">
      < SearchInput 
        setSearchInputs={setSearchInputs} 
        searchInputs={searchInputs}
      />
      < Pokemon 
        currentPokemons={currentPokemons} 
        currentPage={currentPage} 
      />
      < Pagination
        numberOfPages={numberOfPages}
        currentPage={currentPage}
        setCurrentPage={setCurrentPage}
      />
      <Card style={{ height: '3rem', backgroundColor: 'grey'}}>
        <Card.Body>
          <Card.Text>
          Copyright 2023, All rights reserved &copy;
          </Card.Text>
        </Card.Body>
      </Card>
    </div>
  );
}