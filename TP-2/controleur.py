import json
import modele

with open('animal.json', "r") as f:
    animal = json.load(f)
with open('equipement.json', "r") as f:
    equipement = json.load(f)

def nourrir(id_animal):
    if (id_animal in animal):
        if (modele.vérifie_disponibilité('mangeoire') == 'occupe'):
            return 0
        if (modele.lit_etat(id_animal) != 'affame'):
            return 0
        modele.change_lieu(id_animal,'mangeoire')
        modele.change_état(id_animal,'repus')
        return 1
    else:
        return 0
    

def divertir(id_animal):
    if (id_animal in animal):
        if (modele.vérifie_disponibilité('roue') == 'occupe'):
            return 0
        if (modele.lit_etat(id_animal) != 'repus'):
            return 0
        modele.change_lieu(id_animal,'roue')
        modele.change_état(id_animal,'fatigue')
        return 1
    else:
        return 0
    
def coucher(id_animal):
    if (id_animal in animal):
        if (modele.vérifie_disponibilité('nid') == 'occupe'):
            return 0
        if (modele.lit_etat(id_animal) != 'fatigue'):
            return 0
        modele.change_lieu(id_animal,'nid')
        modele.change_état(id_animal,'endormi')
        return 1
    else:
        return 0
    
def reveiller(id_animal):
    if (id_animal in animal):
        if (modele.lit_etat(id_animal) != 'endormi'):
            return 0
        modele.change_lieu(id_animal,'litiere')
        modele.change_état(id_animal,'affame')
        return 1
    else:
        return 0