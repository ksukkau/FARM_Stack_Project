import React, {useState, useEffect, useContext} from 'react';
import axios from 'axios';
import './EditApp.css';
import 'bootstrap/dist/css/bootstrap.min.css'
import { Form, Table, Button, Col, InputGroup, Row, Card, ListGroup } from 'react-bootstrap';
import { SharedStateContext } from './SharedStateContext';

export default function EditApp() {

  const { pokemons, setPokemons } = useContext(SharedStateContext);
  const [pokemon, setPokemon] = useState([]);
  const [pokemonId, setPokemonId] = useState(0);
  const [pokemonName, setPokemonName] = useState('');
  const [pokemonType, setPokemonType] = useState('');
  const [pokemonHP, setPokemonHP] = useState(0);
  const [pokemonAttack, setPokemonAttack] = useState(0);
  const [pokemonDefense, setPokemonDefense] = useState(0);
  const [pokemonSpeed, setPokemonSpeed] = useState(0);
  const [pokemonSpecialAttack, setPokemonSpecialAttack] = useState(0);
  const [pokemonSpecialDefense, setPokemonSpecialDefense] = useState(0);

  const updatePokemonHandler = async () => {
    createPokemon();
    try {
      await axios.post(`http://127.0.0.1:8000/api/v1/pokemon/{id}?p_id=${pokemonId}`, pokemon);
      const updatedPokemons = await axios.get('http://127.0.0.1:8000/api/v1/allpokemon').then(res => res.data);
      setPokemons(updatedPokemons);
    } catch (error) {
      console.error(error);
    }
  };

  const deletePokemonHandler = async () => {
    try {
      await axios.delete(`http://127.0.0.1:8000/api/v1/pokemon/{id}?p_id=${pokemonId}`);
      const updatedPokemons = await axios.get('http://127.0.0.1:8000/api/v1/allpokemon').then(res => res.data);
      setPokemons(updatedPokemons);
    } catch (error) {
      console.error(error);
    }
  };

  const createPokemon = () => {
      let data = {
        "id": pokemonId,
        "name": {
          "english": pokemonName,
          "japanese": "string",
          "chinese": "string",
          "french": "string"
        },
        "type": [
          pokemonType
        ],
        "base": {
          "HP": pokemonHP,
          "Attack": pokemonAttack,
          "Defense": pokemonDefense,
          "Speed": pokemonSpeed,
          "Special Attack": pokemonSpecialAttack,
          "Special Defense": pokemonSpecialDefense
        }
      }
      setPokemon(data)
    }

  return (
    <div className="App">
      <div className='container d-flex justify-content-center align-items-center' style={{padding:'1rem'}}>
        <Card className="align-items-center" style={{width: '50rem', height: '30rem', }}>
          <Card.Header style={{width:'100%'}}>
          <h1 className='text-primary text-center'>Edit Pokemon Data</h1>
          </Card.Header>
          <ListGroup variant="flush">
            <ListGroup.Item>
            <Card.Title>
              <h4 className='text-primary text-center'>Add or Edit Pokemon</h4>
            </Card.Title>
            <Card.Body>
              <div className='form-container'>
                <Form>
                  <Row className="align-items-center">
                  <Col xs="auto">
                      <Form.Label htmlFor="inlineFormInput" visuallyHidden>
                        Pokemon ID
                      </Form.Label>
                      <Form.Control
                        className="mb-2"
                        id="inlineFormInput"
                        placeholder="Pokemon ID"
                        onChange={event => setPokemonId(event.target.value)}
                      />
                    </Col>
                    <Col xs="auto">
                      <Form.Label htmlFor="inlineFormInput" visuallyHidden>
                        Pokemon Name
                      </Form.Label>
                      <Form.Control
                        className="mb-2"
                        id="inlineFormInput"
                        placeholder="Pokemon Name"
                        onChange={event => setPokemonName(event.target.value)}
                      />
                    </Col>
                    <Col xs="auto">
                      <Form.Label htmlFor="inlineFormInput" visuallyHidden>
                        Pokemon Type
                      </Form.Label>
                      <Form.Control
                        className="mb-2"
                        id="inlineFormInput"
                        placeholder="Pokemon Type"
                        onChange={event => setPokemonType(event.target.value)}  
                      />
                    </Col>
                  </Row>
                  <Row className="align-items-center">
                  <Col xs="auto">
                      <Form.Label htmlFor="inlineFormInput" visuallyHidden>
                        HP
                      </Form.Label>
                      <Form.Control
                        className="mb-2"
                        id="inlineFormInput"
                        placeholder="HP"
                        onChange={event => setPokemonHP(event.target.value)}
                      />
                    </Col>
                    <Col xs="auto">
                      <Form.Label htmlFor="inlineFormInput" visuallyHidden>
                        Attack
                      </Form.Label>
                      <Form.Control
                        className="mb-2"
                        id="inlineFormInput"
                        placeholder="Attack"
                        onChange={event => setPokemonAttack(event.target.value)}
                      />
                    </Col>
                    <Col xs="auto">
                      <Form.Label htmlFor="inlineFormInput" visuallyHidden>
                        Defense
                      </Form.Label>
                      <Form.Control
                        className="mb-2"
                        id="inlineFormInput"
                        placeholder="Defense"
                        onChange={event => setPokemonDefense(event.target.value)}
                      />
                    </Col>
                  </Row>
                  <Row className="align-items-center">
                    <Col xs="auto">
                      <Form.Label htmlFor="inlineFormInput" visuallyHidden>
                        Speed
                      </Form.Label>
                      <Form.Control
                        className="mb-2"
                        id="inlineFormInput"
                        placeholder="Speed"
                        onChange={event => setPokemonSpeed(event.target.value)}
                      />
                    </Col>
                    <Col xs="auto">
                      <Form.Label htmlFor="inlineFormInput" visuallyHidden>
                        Special Attack
                      </Form.Label>
                      <Form.Control
                        className="mb-2"
                        id="inlineFormInput"
                        placeholder="Special Attack"
                        onChange={event => setPokemonSpecialAttack(event.target.value)}
                      />
                    </Col>
                    <Col xs="auto">
                      <Form.Label htmlFor="inlineFormInput" visuallyHidden>
                        Special Defense
                      </Form.Label>
                      <Form.Control
                        className="mb-2"
                        id="inlineFormInput"
                        placeholder="Special Defense"
                        onChange={event => setPokemonSpecialDefense(event.target.value)}
                      />
                    </Col>
                  </Row>
                  <Row className="align-items-center"> 
                    <Col xs="auto">
                      <Button type="button" className="mb-2" onClick={updatePokemonHandler}>
                        Submit
                      </Button>
                    </Col>
                  </Row>
                </Form>
              </div>
            </Card.Body>
            </ListGroup.Item>
            <ListGroup.Item>
              <Card.Title>
                <h4 className='text-primary text-center'>Delete Pokemon</h4> 
              </Card.Title>
              <Card.Body>
              <div className='form-container'>
                <Form>
                  <Row className="align-items-center">
                    <Col xs="auto">
                      <Form.Label htmlFor="inlineFormInput" visuallyHidden>
                        Pokemon ID
                      </Form.Label>
                      <Form.Control
                        className="mb-2"
                        id="inlineFormInput"
                        placeholder="Pokemon ID"
                        onChange={event => setPokemonId(event.target.value)}
                      />
                    </Col>
                    <Col xs="auto">
                      <Button type="button" className="mb-2" onClick={deletePokemonHandler}>
                        Delete
                      </Button>
                      </Col>
                  </Row>
                </Form>
              </div>
              </Card.Body>
            </ListGroup.Item>
          </ListGroup>
        </Card>
      </div>
      <div className='container d-flex justify-content-center align-items-center' style={{padding:'1rem'}}>
      <div className='row' style={{width:'80%'}}>
          <div className='col-md-12'>
            <h1 className='text-primary text-center'>Pokemon List</h1>
            <div className='table-responsive'>
              <Table>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Type</th>
                    <th>Stats</th>
                  </tr>
                </thead>
                <tbody>
                  {pokemons.length > 0 && pokemons.map((pokemon, index) => (
                    <tr key={index}>
                      <td>{pokemon.name.english}</td>
                      <td>{pokemon.type}</td>
                      <td>
                        <ul id="statList">
                          {(JSON.stringify(pokemon.base).replace('{', '').replace('}', '').split(',')).map((stat, index) => (
                        <li key={index}>{stat.replaceAll('"', '')}</li>
                        ))}
                        </ul> 
                        </td>
                    </tr>
                  ))}
                </tbody> 
              </Table>
            </div>
          </div>
        </div>
      </div>
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