# FARM_Stack_Project

[![Custom Cloud Status](https://status.customcloud.ca/api/badge/10/status)](https://status.customcloud.ca/status/farmstack)
 
Challenges: Faced significant challenges in defining data to match the data provided, specifically with the space in special attack and special defense, using alias was not inserting into database correctly, edited dicts before insertion to resolve, alias allows reading correctly, this resolved issue.

# ASSIGNMENT 1 POKEMON API

## SCHEMA RULES

  * id: Number
  * name: must be an Object
    * english: String
    * japanese: String
    * chinese: String
    * french: String
  * type: List[String]
  * base: must be an Object
    * HP: Integer
    * Attack: Integer
    * Defense: Integer
    * Speed: Integer
    * Special Attack: Integer
    * Special Defense: Integer
     

## SERVER ROUTES

### GET ALL POKEMON

  Retrives all database records. 

* #### URL 
  `/api/v1/allpokemon`
  
* #### METHOD
   `GET`

* #### URL PARAMS
  none
  
* #### BODY PARAMS
  none
  
* #### RESPONSES
  ##### SUCCESS 
  * Code: 200 <br />
    Content: {`List of all Pokemon`}

* #### SAMPLE REQUESTS
  `{{URL}}allpokemon`
  
    
### CREATE A NEW POKEMON

  Adds a new Pokemon to the database.

* #### URL 
  `/api/v1/pokemon`
  
* #### METHOD
   `POST`

* #### URL PARAMS
  ##### Required 
  * `after=[integer]`
  * `count=[integer]`
  
* #### BODY PARAMS
  ##### Required 
  JSON 
  * id: Number, Unique = True
  * name: must be an Object
    * english: String, max 20 Char
    * japanese: String
    * chinese: String
    * french: String
  * type: String, enum: possibleTypes
  * base: must be an Object
    * HP: Number
    * Attack: Number
    * Defense: Number 
    * Speed: Number
    * Special Attack: Number 
    * Special Defense: Number
  
* #### RESPONSES
  ##### SUCCESS 
  * Code: 200 <br />
    Content: `{Submitted pokemon Json}`
    
  ##### ERROR
  * Code: 400 <br />
    Content: `{"msg": "Pokemon id 900000 already exists"}`
  * Code: 400 <br />
    Content: `{"msg": "error message"}`

* #### SAMPLE REQUESTS
    `{{URL}}/api/v1/pokemon`
  * body:  
    `{  
    "name": {  
      "english": "New Pokemon",  
      "japanese": "フシギバナ",  
      "chinese": "妙蛙花",
      "french": "Florizarre"
    },
    "base": {
      "HP": 80,
      "Attack": 82,
      "Defense": 83,
      "Speed": 80,
      "Special Attack": 100,
      "Special Defense": 100
    },
    "id": 9000,
    "type": [
      "Grass",
      "Poison"
    ]
  }`
  
    
### GET A POKEMON BY ID

  Fetches single record using pokemon id.

* #### URL 
  '/api/v1/pokemon/:id'
  
* #### METHOD
   `GET`

* #### URL PARAMS
  ##### Required 
  * `id=[integer]`
  
* #### BODY PARAMS
  none
  
* #### RESPONSES
  ##### SUCCESS 
  * Code: 200 <br />
    Content: `{Submitted id pokemon Json}`
  * Code: 200 <br />
    Content: `{"msg": "Pokemon id < id > does not exist"}`
    
  ##### ERROR
  * Code: 400 <br />
    Content: `{"msg": "Request failed: Id should be a number"}`

* #### SAMPLE REQUESTS
    `{{URL}}pokemon/3`
    

### UPSERT POKEMON DOCUMENT 

  Inserts or updates pokemon, requires full pokemon document.

* #### URL 
  '/api/v1/pokemon/:id'
  
* #### METHOD
   `POST`

* #### URL PARAMS
  ##### Required 
  * `id=[integer]`
  
* #### BODY PARAMS
  ##### Required 
  JSON 
  * id: Number, Unique = True
  * name: must be an Object
    * english: String, max 20 Char
    * japanese: String
    * chinese: String
    * french: String
  * type: String, enum: possibleTypes
  * base: must be an Object
    * HP: Number
    * Attack: Number
    * Defense: Number 
    * Speed: Number
    * Special Attack: Number 
    * Special Defense: Number
  
* #### RESPONSES
  ##### SUCCESS 
  * Code: 200 <br />
    Content: `{Pokemon id < id > updated successfully}`
  * Code: 200 <br />
    Content: `{"msg": "Pokemon id < id > does not exist"}`
    
  ##### ERROR
  * Code: 400 <br />
    Content: `{"msg": "Request failed: Id should be a number"}`

* #### SAMPLE REQUESTS
    `{{URL}}/api/v1/pokemon/3`
  * body:  
    `{  
    "name": {  
      "english": "New Pokemon",  
      "japanese": "フシギバナ",  
      "chinese": "妙蛙花",
      "french": "Florizarre"
    },
    "base": {
      "HP": 80,
      "Attack": 82,
      "Defense": 83,
      "Speed": 80,
      "Special Attack": 100,
      "Special Defense": 100
    },
    "id": 9000,
    "type": [
      "Grass",
      "Poison"
    ]
  }`
  
  
  ### UPDATE POKEMON DOCUMENT 

  Updates pokemon, does not require full pokemon document.

* #### URL 
  '/api/v1/pokemon/:id'
  
* #### METHOD
   `PUT`

* #### URL PARAMS
  ##### Required 
  * `id=[integer]`
  
* #### BODY PARAMS
  ##### OPTIONAL
  JSON 
  * id: Number, Unique = True
  * name: must be an Object
    * english: String, max 20 Char
    * japanese: String
    * chinese: String
    * french: String
  * type: String, enum: possibleTypes
  * base: must be an Object
    * HP: Number
    * Attack: Number
    * Defense: Number 
    * Speed: Number
    * Special Attack: Number 
    * Special Defense: Number
  
* #### RESPONSES
  ##### SUCCESS 
  * Code: 200 <br />
    Content: `{Pokemon id < id > updated successfully}`
  * Code: 200 <br />
    Content: `{"msg": "Pokemon id 9000909 does not exist, no update performed"}`
    
  ##### ERROR
  * Code: 400 <br />
    Content: `{"msg": "Request failed: Id should be a number"}`

* #### SAMPLE REQUESTS
    `{{URL}}/api/v1/pokemon/3`
  * body:  
    `{ 
    "type": [
      "Grass",
      "Poison"
  }`
  
    
### DELETE POKEMON BY ID

  Deletes single record using pokemon id.

* #### URL 
  '/api/v1/pokemon/:id'
  
* #### METHOD
   `DELETE`

* #### URL PARAMS
  ##### Required 
  * `id=[integer]`
  
* #### BODY PARAMS
  none
  
* #### RESPONSES
  ##### SUCCESS 
  * Code: 200 <br />
    Content: `{"msg": "Pokemon id < id > deleted successfully"}`
  * Code: 200 <br />
    Content: `{"msg": "Pokemon id < id > does not exist"}`
    
  ##### ERROR
  * Code: 400 <br />
    Content: `{"msg": "Request failed: Id should be a number"}`

* #### SAMPLE REQUESTS
    `{{URL}}pokemon/3`
