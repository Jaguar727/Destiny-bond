import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bs4 import BeautifulSoup
from urllib.request import urlopen
from typing import List, NamedTuple
from unidecode import unidecode

load_dotenv()

connection_string=os.getenv("MONGODB_CONNECTION_STRING")

client = MongoClient(connection_string)
db = client.pokedex_vue
pokemon_collection = db.pokemons

response = urlopen('https://www.serebii.net/pokemon/nationalpokedex.shtml')
html = response.read().decode('latin-1')
soup = BeautifulSoup(html, 'html.parser')

pokedex = soup.find('table', {'class' : 'dextable'}).findAll('tr',recursive=False)

def idConverter (id):
    convertedId = int(id.replace('#',''))
    return convertedId

def handlePokemonName (name):
    correctedName = (unidecode(name.replace('♂', 'm').replace('♀', 'f').replace(' ','').lower()))
    return correctedName

class Pokemon(NamedTuple):
    id: str
    intId: int
    name: str
    urlName: str
    icon: str
    types: List[str]
    abilities: List[str]
    hp: int
    attack: int
    defense: int
    sp_attack: int
    sp_defense: int
    speed: int

scraped_counter = 0

for row in pokedex[2:]:
    pokemon = {}
    pkm = row.findAll('td', {'class': 'fooinfo'})

    pokemon['id']  = pkm[0].getText()
    pokemon['id'] = pokemon['id'].replace('\t', '').replace('\n', '').replace('\r', '')
    pokemon['icon'] = pkm[1].find('img')['src']
    pokemon['name'] = pkm[2].find('a').getText()
    pokemon['types'] = pkm[3].findAll('img')
    cont = 0

    for type in pokemon['types']:
        pokemon['types'][cont] = type['src'][17:-4]
        cont = cont + 1
        
    
    cont = 0
    pokemon['abilities'] = pkm[4].findAll('a')
    
    for ability in pokemon['abilities']:
        pokemon['abilities'][cont] = ability.getText()
        cont = cont + 1
    
    pokemon['hp']  = pkm[5].getText()
    pokemon['attack']  = pkm[6].getText()
    pokemon['defense']  = pkm[7].getText()
    pokemon['sp_attack']  = pkm[8].getText()
    pokemon['sp_defense']  = pkm[9].getText()
    pokemon['speed']  = pkm[10].getText()
    pokemon['urlName'] = handlePokemonName (pokemon['name'])
    pokemon['intId'] = idConverter (pokemon['id'])

    pokemon_data = Pokemon(
        id = pokemon['id'],
        name = pokemon['name'],
        urlName = pokemon['urlName'],
        intId = pokemon['intId'],
        icon = pokemon['icon'],
        types = pokemon['types'],
        abilities = pokemon['abilities'],
        hp = pokemon['hp'],
        attack = pokemon['attack'],
        defense = pokemon['defense'],
        sp_attack = pokemon['sp_attack'],
        sp_defense = pokemon['sp_defense'],
        speed = pokemon['speed'],
    )
    
    pokemon_collection.insert_one({
        "id": pokemon_data.id,
        "intId": pokemon_data.intId,
        "name": pokemon_data.name,
        "urlName": pokemon_data.urlName,
        "icon": pokemon_data.icon,
        "types": pokemon_data.types,
        "abilities": pokemon_data.abilities,
        "hp": int(pokemon_data.hp),
        "attack": int(pokemon_data.attack),
        "defense": int(pokemon_data.defense),
        "sp_attack": int(pokemon_data.sp_attack),
        "sp_defense": int(pokemon_data.sp_defense),
        "speed": int(pokemon_data.speed)
        })
    

    scraped_counter+=1

    print(pokemon)
    print("Pokémon scraped: ", scraped_counter)

print("Done! Successfully scraped", scraped_counter, "Pokémon!")