import {useState} from 'react'
import React from 'react'
import './SearchInput.css';

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
    <div class="formContainer">

        <div id="searchcontainer">
          <div id="namecontainer">Name:</div> 
          <input
          type="text"
          placeholder="Search..."
          id='search'
          onChange={textOnChangeFunctionHandle}
          />
        </div>

        <div id ="typescontainer">
          <div id="typetitle">Select Type</div>
          <ul id="typeList" >
          {
          pokemonTypes.map((name, index) => {
            return (
              <li key={index}>
                <div className="typeitem">
                  <div className="left-section">
                    <input
                      type="checkbox"
                      id={`custom-checkbox-${index}`}
                      name={name}
                      value={name}
                      key={name}
                      onChange={() => handleOnChange(index)}
                    />
                    <label htmlFor={`custom-checkbox-${index}`}>{name}</label>
                  </div>
                </div>
              </li>
            );
          })
          }
          </ul>
        </div>

        <div id="sliderContainer">
          <div class="slider">
            <label for="rangeHp">Hp:</label>
            <input id="rangeHp" 
            type="range" 
            min="0" 
            max="255" 
            step="1" 
            onChange={handleHpSlider}
            value={hpState}
            />
            <p id='valueHp'>{hpState}</p>
          </div>
          <div class="slider">
            <label for="rangeAttack">Attack:</label>
            <input id="rangeAttack" 
            type="range" 
            min="0" 
            max="255" 
            step="1" 
            onChange={handleAkSlider}
            value={akState}/>
              <p id="valueAttack">{akState}</p>
          </div>
        </div>

    </div>
  )

}