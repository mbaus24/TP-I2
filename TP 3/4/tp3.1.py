from pony import orm
import json
 
from pony import orm


db = orm.Database()
 
class Equipement(db.Entity):
    id_equip = orm.PrimaryKey(str)
    disponibilité = orm.Required(str)
 
class Animal(db.Entity):
    id_animal = orm.PrimaryKey(str)
    lieu = orm.Required(Equipement)
    état = orm.Required(str)
    race = orm.Required(str)
    type = orm.Required(str)
    
    

 
db.bind(provider='sqlite', filename='animalerie.db', create_db=True)
db.generate_mapping(create_tables=True)
 
équipement_data = 'équipement.json'
with open(équipement_data, "r") as f:
    équipement_dict = json.load(f)
    for id_équip in équipement_dict:
        disponibilité = équipement_dict[id_équip]["DISPONIBILITÉ"]
        with orm.db_session:
            try:
                Equipement(id_équip=id_équip, disponibilité=disponibilité)
                orm.commit()
            except:
                print(id_équip, "already exists in database")
                pass
 
 
animal_data = 'animal.json'
with open(animal_data, "r") as f:
    animal_dict = json.load(f)
    for id_animal in animal_dict:
        état = animal_dict[id_animal]["ETAT"]
        type = animal_dict[id_animal]["TYPE"]
        race = animal_dict[id_animal]["RACE"]
        lieu = animal_dict[id_animal]["LIEU"]
        with orm.db_session:
            try:
                Animal(id_animal=id_animal,
                       état=état,
                       type=type,
                       race=race,
                       lieu=Equipement[lieu])
                orm.commit()
            except:
                print(id_animal, "already exists in database")
                pass