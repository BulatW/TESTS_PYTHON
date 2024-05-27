import requests
URL= "https://api.pokemonbattle.me/v2"
TOKEN="f2b2c75309eaf2443fee67859c5fc3cc"
HEADER={"Content-Type":"application/json","trainer_token":TOKEN}
TRAINER_ID= '2506'

body={ "trainer_token": TOKEN,
               "email": "german@dolnikov.ru",
            "password": "Iloveqa1" }

body_confirmation={ "trainer_token": TOKEN}

body_create={ "name": "generate",
             "photo": "generate"}

# response=requests.post(url=f"{URL}/trainers/reg",headers=HEADER, json=body)
# print(response.text )
# response_confirmation=requests.post(url=f"{URL}/trainers/confirm_email",headers=HEADER,json=body_confirmation)
# print(response_confirmation.text)


# ВЫПОЛНЕНИЕ ДОМАШНЕГО ЗАДАНИЯ:


response_create=requests.post(url=f"{URL}/pokemons",headers=HEADER,json=body_create)
print(response_create.text)

pokemon_id=response_create.json()['id']

body_add=   {"pokemon_id": pokemon_id}

body_change={"pokemon_id": pokemon_id,
                   "name": "generate"}

response_change=requests.patch(url=f"{URL}/pokemons",headers=HEADER,json=body_change)
print(response_change.text)

response_add=requests.post(url=f"{URL}/trainers/add_pokeball",headers=HEADER,json=body_add)
print(response_add.text)




# response_get=requests.get(url=f'{URL}/pokemons',headers=HEADER,params={'trainer_id':TRAINER_ID})

# pokemon_id=response_create.json()['id']
# print(pokemon_id)

# message=response_get.json()['name']=='Officer'
# print(message)