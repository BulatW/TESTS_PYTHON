import requests
import pytest

URL= "https://api.pokemonbattle.me/v2"
TOKEN="f2b2c75309eaf2443fee67859c5fc3cc"
HEADER={"Content-Type":"application/json","trainer_token":TOKEN}
TRAINER_ID= '2506'

def test_status_code():
    response=requests.get(url=f'{URL}/pokemons', params={'trainer_id':TRAINER_ID})
    assert response.status_code==200

def test_partOfResponse():
    response_get=requests.get(url=f'{URL}/pokemons', params={'trainer_id':TRAINER_ID})
    assert response_get.json()['data'][0]['name']=='carnivine'

@pytest.mark.parametrize('key,value',[('name','carnivine'),('trainer_id',TRAINER_ID),('id','28038')])
def test_parametrize(key,value):
    response_parametrize=requests.get(url=f'{URL}/pokemons', params={'trainer_id':TRAINER_ID})
    assert response_parametrize.json()['data'][0][key]==value


# ВЫПОЛНЕНИЕ ДОМАШНЕГО ЗАДАНИЯ:

def test_status_code():
    response_trainers=requests.get(url=f'{URL}/trainers',headers=HEADER)
    assert response_trainers.status_code==200 

def test_partOfResponse():
    response_get=requests.get(url=f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name']=='Sam'