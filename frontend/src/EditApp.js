import React, {useState, useEffect, useContext} from 'react';
import axios from 'axios';
import './EditApp.css';
import 'bootstrap/dist/css/bootstrap.min.css'
import Card from 'react-bootstrap/Card';
import { Table } from 'react-bootstrap';
import { SharedStateContext } from './SharedStateContext';

export default function EditApp() {

  const { pokemons } = useContext(SharedStateContext);
  console.log(pokemons);
  return (
    <div className="App">
      <div className='container'>
        <div className='row'>
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

