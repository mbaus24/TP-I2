import json


with open('animal.json', "r") as f:
    animal = json.load(f)
with open('equipement.json', "r") as f:
    equipement = json.load(f)


def lit_race(animal_id):
    if (animal_id in animal):
        return animal[animal_id]['RACE']
    else:
        print('Désolé ', animal_id, ' n"est pas un animal connu')
        return None
    


def lit_etat(animal_id):
    if (animal_id in animal):
        return animal[animal_id]['ETAT']
    else:
        print('Désolé ', animal_id, ' n"est pas un animal connu')
        return None
    
def lit_lieu(animal_id):
    if (animal_id in animal):
        return animal[animal_id]['LIEU']
    else:

        print('Désolé ', animal_id, ' n"est pas un animal connu')
        return None
    

def vérifie_disponibilité(equipement_id):
    if (equipement_id in equipement):
        return equipement[equipement_id]['DISPONIBILITE']
    else:
        print('Désolé ', equipement_id, ' n"est pas un équipement connu')
        return None

def cherche_occupant(lieu):
    if (lieu in equipement):
        liste = []
        for animals in animal:
            if(lit_lieu(animals) == lieu):
                liste.append(animals)
        if (liste == []):
            print('Désolé, le lieu ',lieu,'est vide')
            return liste
        return liste
                            
            
            
            
            

def change_état(id_animal, état):
    print('Changement de l"état de l"animal', id_animal,'en l"état',état)
    etat_autorises = ['fatigue','affame','endormi','repus']
    if (état in etat_autorises) & (id_animal in animal):
        animal[id_animal]['ETAT'] = état
    else:
        print('Désolé, ', état, 'n"est pas un état autorisé ou l"animal',id_animal,'est incorrect')
    return None   

def change_lieu(id_animal,lieu):
    if (lit_lieu(id_animal) == lieu):
        print('L"animal ',id_animal,'est déjà dans le lieu',lieu)
        return None
    else:
        if (id_animal in animal) & (lieu in equipement):
            if (vérifie_disponibilité(lieu) == 'occupe'):
                print('Désolé, le lieu ',lieu,'est occupe')
                return None
            else:
                ancien_lieu = lit_lieu(id_animal)
                equipement[lit_lieu(id_animal)]['DISPONIBILITE'] = 'libre'
                animal[id_animal]['LIEU'] = lieu
                if (lieu != 'litiere'):
                    equipement[lieu]['DISPONIBILITE'] = 'occupe'
                print('L"animal',id_animal,' est passé de ',ancien_lieu,'à',lieu,' avec succès')
        else:
            print('Désolé ', id_animal, ' n"est pas un animal connu ou ',lieu,'n"est pas un équipement correct')
        return None

