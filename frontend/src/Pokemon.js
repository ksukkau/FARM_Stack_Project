import React from 'react'
import './Pokemon.css';
import { useState } from 'react'


export default function Pokemon(
  { currentPokemons,
  currentPage }) 
{

  const [element, setelement] = useState();
  


  const createNewDiv = (item, imgurl) => {
    let stats = JSON.stringify(item.base).replace('{', '').replace('}','').split(',')
    let type = item.type
    let typeString =''
    type.map(item => {
      typeString = typeString + item + ' '
    })
    console.log(typeString)
    const newElement = (
      <div id='details'>
      <div>
      <h4>Pokemon Detail:</h4>
      <p>ID: {item.id}</p>
      <p>Name: {item.name.english}</p>
      <p>Type: {typeString}</p>
      <ul id='statList'>
        <li>{stats[0].replaceAll('"', '')}</li>
        <li>{stats[1].replaceAll('"', '')}</li>
        <li>{stats[2].replaceAll('"', '')}</li>
        <li>{stats[3].replaceAll('"', '')}</li>
        <li>{stats[4].replaceAll('"', '')}</li>
        <li>{stats[5].replaceAll('"', '')}</li>
      </ul>
      </div>
      <div> 
        <img src={imgurl}crossOrigin='Anonymous' 
        id='detailpokeimg'></img>
      </div>
      </div>
    )
    setelement(newElement);
  }

  // if(element){
  //   console.log('element')
  //   //setelement('')
  // }

  return (
    <div id="outsidecards">
      {element}
    <div class='cards'>
    {
      currentPokemons.map(item => {
        let itemid = String(item.id)
        let imageID = itemid.padStart(3, '0')
        let imgurl = `https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/${imageID}.png`
        // console.log(imageID)
        return (
        <div key={item.id} class='card' onClick={()=>createNewDiv(item, imgurl)}>  
        <div class='cardtext'>{item.name.english} ID: {item.id} </div>
        <div class='imgdiv'>
        <img  src={imgurl} 
        crossOrigin='Anonymous' 
        id='pokeimg'></img>
        </div>
        </div>)
      })
    }
  </div>
  </div>
  )


}