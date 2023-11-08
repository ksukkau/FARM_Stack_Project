import React, { useState, createContext } from 'react';

export const SharedStateContext = createContext();

export const SharedStateProvider = ({ children }) => {
  const [pokemons, setPokemons] = useState([]);

  return (
    <SharedStateContext.Provider value={{ pokemons, setPokemons }}>
      {children}
    </SharedStateContext.Provider>
  );
};