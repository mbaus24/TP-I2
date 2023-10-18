from pony import orm
from data_model import Equipement, Animal, db
 
liste_etats = ['affame', 'fatigue', 'repus', 'endormi']
liste_equipement= ['litiere', 'mangeoire', 'roue', 'nid']
db.bind(provider='sqlite', filename='animalerie.db')
db.generate_mapping()



def lit_etat(id_animal):
    with orm.db_session:
        try:
            return Animal[id_animal].etat
        except:
            return None
 
def lit_lieu(id_animal):
    with orm.db_session:
        try:
            return Animal[id_animal].lieu
        except:
            return None
        
def verifie_disponibilite(equipement_id):
    with orm.db_session:
        try:
            return Equipement[equipement_id].disponibilite
        except:
            return None
        

def cherche_occupant(equipement_id):
    with orm.db_session:
        if equipement_id in liste_equipement:
            try:
                return Equipement[equipement_id].animal
            except:
                return None
        else:
            return [ ]

def change_etat(id_animal, etat):
    if etat in liste_etats:
        with orm.db_session:
            try:
                Animal[id_animal].etat = etat
            except:
                return None
    else:
        return None                         
            
            
            
            
def change_lieu(id_animal, lieu):
    if lieu in liste_equipement:
        if (verifie_disponibilite(lieu) == 'occupe'):
            print('Desole, le lieu ',lieu,'est occupe')
            return None
        with orm.db_session:
            try:
                Animal[id_animal].lieu = Equipement[lieu]
            except:
                return None
    else:
        return None

# def change_lieu(id_animal,lieu):
#     if (lit_lieu(id_animal) == lieu):
#         print('L"animal ',id_animal,'est dejà dans le lieu',lieu)
#         return None
#     else:
#         if (id_animal in animal) & (lieu in equipement):
#             if (verifie_disponibilite(lieu) == 'occupe'):
#                 print('Desole, le lieu ',lieu,'est occupe')
#                 return None
#             else:
#                 ancien_lieu = lit_lieu(id_animal)
#                 equipement[lit_lieu(id_animal)]['DISPONIBILITE'] = 'libre'
#                 animal[id_animal]['LIEU'] = lieu
#                 if (lieu != 'litiere'):
#                     equipement[lieu]['DISPONIBILITE'] = 'occupe'
#                 print('L"animal',id_animal,' est passe de ',ancien_lieu,'à',lieu,' avec succes')
#         else:
#             print('Desole ', id_animal, ' n"est pas un animal connu ou ',lieu,'n"est pas un equipement correct')
#         return None

