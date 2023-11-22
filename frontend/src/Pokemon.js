import React, { useState } from 'react';
import './css/Pokemon.css';

export default function Pokemon({ currentPokemons, currentPage }) {
  const [element, setElement] = useState(null);

  const createNewDiv = (item, imgurl) => {
    let stats = JSON.stringify(item.base).replace('{', '').replace('}', '').split(',');
    let type = item.type;
    let typeString = '';
    type.forEach((item) => {
      typeString = typeString + item + ' ';
    });

    const newElement = (
      <div id="details" onClick={() => setElement(null)}>
        <div>
          <h4>Pokemon Detail:</h4>
          <p>ID: {item.id}</p>
          <p>Name: {item.name.english}</p>
          <p>Type: {typeString}</p>
          <ul id="statList">
            {stats.map((stat, index) => (
              <li key={index}>{stat.replaceAll('"', '')}</li>
            ))}
          </ul>
        </div>
        <div>
          <img src={imgurl} crossOrigin="Anonymous" id="detailpokeimg" alt={item.name.english} />
        </div>
      </div>
    );

    setElement(newElement);
  };

  return (
    <div id="outsidecards">
      {element}
      <div className="cards">
        {currentPokemons.map((item) => {
          let itemid = String(item.id);
          let imageID = itemid.padStart(3, '0');
          let imgurl = `https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/${imageID}.png`;

          return (
            <div key={item.id} className="card" onClick={() => createNewDiv(item, imgurl)}>
              <div className="cardtext">
                {item.name.english} ID: {item.id}
              </div>
              <div className="imgdiv">
                <img src={imgurl} crossOrigin="Anonymous" id="pokeimg" alt={item.name.english} />
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
