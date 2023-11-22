import {useState} from 'react'
import React from 'react'
import './css/SearchInput.css';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import FloatingLabel from 'react-bootstrap/esm/FloatingLabel';
import Container from 'react-bootstrap/Container';


export default function SearchInput(
  { searchInputs, setSearchInputs }) 
{
  const pokemonTypes = [  
    'Normal',   
    'Fighting',
    'Flying',   
    'Poison',
    'Ground',   
    'Rock',
    'Bug',      
    'Ghost',
    'Steel',    
    'Fire',
    'Water',    
    'Grass',
    'Electric', 
    'Psychic',
    'Ice',      
    'Dragon',
    'Dark',     
    'Fairy'
  ]

  let selectedTypes = []

  const [hpState, setHpSliderState] = useState(255);

  const [akState, setAkSliderState] = useState(255);

  const [checkedState, setCheckedState] = useState(
    new Array(pokemonTypes.length).fill(false)
    );

  const textOnChangeFunctionHandle = (e) => {
    setSearchInputs({ ...searchInputs, name: e.target.value })
    // console.log(searchInputs)
  }

  const handleHpSlider = (e) => {
    setHpSliderState(e.target.value);
    setSearchInputs({...searchInputs, hp: e.target.value})
    // console.log(hpState)
  };
  
  const handleAkSlider = (e) => {
    setAkSliderState(e.target.value)
    setSearchInputs({...searchInputs, attack: e.target.value})
    // console.log(akState)
  };

  const handleOnChange = (position) => {
    const updatedCheckedState = checkedState.map((item, index) =>
      index === position ? !item : item
    )
    // console.log(updatedCheckedState)
    // console.log(checkedState)
    setCheckedState(updatedCheckedState)
    for( let i = 0; i < checkedState.length; i++){
      if(updatedCheckedState[i]){
        selectedTypes.push(pokemonTypes[i])
      }
    }
    // console.log(selectedTypes)
    setSearchInputs({ ...searchInputs, type: selectedTypes})
    selectedTypes = []
  };


 return (

    <Form>
      <Form.Label className="mt-3" column="lg" >Pokemon Search</Form.Label>
      <Container fluid='md'>
      <Row>
        <Col lg={5} >
        <FloatingLabel controlID="floatingName" label="Pokemon Name" className="m-auto">
        <Form.Control type="text" placeholder="Search..." onChange={textOnChangeFunctionHandle}/>
        </FloatingLabel>
        </Col>
      </Row>
      <Row className="justify-content-md-start">
        <Form.Label className="mt-3" column="lg" >Select Type</Form.Label>
      </Row>
      <Row>
        <Col className="m-2 justify-content-start align-items-start">
        {
          pokemonTypes.map((name, index) => {
            return (
                    <Form.Check
                      inline
                      type="checkbox"
                      id={`custom-checkbox-${index}`}
                      name={name}
                      value={name}
                      key={name}
                      onChange={() => handleOnChange(index)}
                      label={name}
                    />
            );
          })
          }
        </Col>
      </Row>
      <Row className="d-flex justify-content-center align-items-center">
        <Col lg={5}>
          <Form.Label className="m-3">Hp:</Form.Label>
          <Form.Range min="0" max="255" step="1" onChange={handleHpSlider} value={hpState}/>
          <p id='valueHp'>{hpState}</p>
        </Col>
        <Col lg={5}>
          <Form.Label className="m-3">Attack:</Form.Label>
          <Form.Range min="0" max="255" step="1" onChange={handleAkSlider} value={akState}/>
          <p id="valueAttack">{akState}</p>
        </Col>
      </Row>
      </Container>
    </Form>
  )
}