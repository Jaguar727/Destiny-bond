import os
from urllib import response
from dotenv import load_dotenv
from pymongo import MongoClient
from bs4 import BeautifulSoup
from urllib.request import urlopen
from unidecode import unidecode
from typing import NamedTuple

load_dotenv()

connection_string=os.getenv("MONGODB_CONNECTION_STRING")

response = urlopen('https://www.serebii.net/pokemon/')
html = response.read().decode('latin-1')
soup = BeautifulSoup(html, 'html.parser')

client = MongoClient(connection_string)
db = client.pokedex_vue
pokemon_collection = db.pokemons
class PkmImg(NamedTuple):
    img: str

pages = []

for pkm in pokemon_collection.find({}, {"_id": 0, "urlName": 1}):
    currentLink = ('https://www.serebii.net/pokemon/' + pkm['urlName'] + '/')
    pages.append(currentLink)

allPkmImg = []


for page in pages:
    response = urlopen(page)
    html = response.read().decode('latin-1')
    soup = BeautifulSoup(html, 'html.parser')
    pokemonTable = soup.find('table', {'class':'dextable'})
    img = pokemonTable.find('td', {'class':'fooinfo'}).find('img')['src']
    allPkmImg.append(img)

cont = 1

for image in allPkmImg:
    pokemon_data = PkmImg(
        img = image
    )
    pokemon_collection.update_one({'intId': cont}, {'$set':{'artwork': pokemon_data.img}})
    print(cont + ' Imagens adicionadas a db')
    cont +=1
    
    


        
        


