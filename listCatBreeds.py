import requests
import json

f = open('catBreeds.txt', 'w')
r = requests.get('https://catfact.ninja/breeds')
rJSON = json.loads(r.text)
catBreedArray = rJSON["data"]

print(catBreedArray)

for breed in catBreedArray:
    print(breed)
    print(breed["breed"])
    f.write("breed: " + breed["breed"] + " | country: " + breed["country"] + " | origin: " + breed["origin"] + " | coat" + breed["coat"] + " | pattern: " + breed["pattern"] + "\n")