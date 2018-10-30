with open('L_Etudiants.csv', 'r') as csvfile:
    csv = csvfile.readlines()

final = [
    {
        "model" : "charpak.promo",
        "pk": 1,
        "fields": {
            "nom": "2016",
            "couleur": "bleu"
        }
    }, 
    {
        "model" : "charpak.promo",
        "pk": 2,
        "fields": {
            "nom": "2017",
            "couleur": "bleu"
        }
    },
    {
        "model" : "charpak.promo",
        "pk": 3,
        "fields": {
            "nom": "2018",
            "couleur": "bleu"
        }
    },
    {
        "model" : "charpak.promo",
        "pk": 4,
        "fields": {
            "nom": "2019",
            "couleur": "bleu"
        }
    },
    {
        "model" : "charpak.promo",
        "pk": 5,
        "fields": {
            "nom": "2020",
            "couleur": "bleu"
    }
    },
    {
        "model" : "charpak.promo",
        "pk": 6,
        "fields": {
            "nom": "2021",
            "couleur": "bleu"
        }
    }
]
i = 0
for line in csv[1:]:
    i += 1
    promo, nom, prenom = line.replace('\n','').split(';')
    promo = int(promo) - 2015
    final.append({
        "model":"charpak.etudiant",
        "pk":i,
        "fields":{
            "nom": nom,
            "prenom":prenom,
            "promo":promo
            }
        })

import json

with open('fixtures.json', mode='w') as f:
    json.dump(final, f, indent=4)
    
"""
[
  {
    "model": "myapp.person",
    "pk": 1,
    "fields": {
      "first_name": "John",
      "last_name": "Lennon"
    }
  },
  {
    "model": "myapp.person",
    "pk": 2,
    "fields": {
      "first_name": "Paul",
      "last_name": "McCartney"
    }
  }
]
"""


    
