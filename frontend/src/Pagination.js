import React from 'react'
import './Pagination.css'

function range(start, end) {
  var ans = [];
  for (let i = start; i <= end; i++) {
      ans.push(i);
  }
  return ans;
}



export default function Pagination({ numberOfPages, currentPage, setCurrentPage }) {
  const pageNumbers = []

  for (let i = 1; i <= numberOfPages; i++) {
    pageNumbers.push(i)
    
  }

  const nextPage = () => {
    if (currentPage !== numberOfPages) setCurrentPage(currentPage + 1)
  }

  const prevPage = () => {
    if (currentPage !== 1) setCurrentPage(currentPage - 1)
  }

  let thischunk;
  for(let i=1; i <= 81; i+=10){
    const chunk = range(i, i+9)
    if(chunk.includes(currentPage)){
      thischunk = chunk
    }
  }
  

  return (
    <div class='button-holder'>
      {(currentPage !== 1) && (<button class = 'button' id='prev' onClick={prevPage}>prev </button>)}

      {
        thischunk.map(number => {
          if(number === currentPage){
            return (<>
              <button id ='current' class = 'button' onClick={() => setCurrentPage(number)}>
                {number}
              </button>
            </>)
          } else if(number<=numberOfPages){
            return (<>
              <button class = 'button' onClick={() => setCurrentPage(number)}>
                {number}
              </button>
            </>)
          }
        })
      }
      {(currentPage !== numberOfPages && numberOfPages > 0)&&<button class = 'button' id='next' onClick={nextPage}>next</button>}
    </div>
  )
}

