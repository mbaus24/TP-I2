import json
 
from pony import orm
from data_model import Equipement, Animal, db
 
db.bind(provider='sqlite', filename='animalerie.db', create_db=True)
orm.set_sql_debug(True)
db.generate_mapping(create_tables=True)
 
equipement_data = 'TP-4/equipement.json'
with open(equipement_data, "r") as f:
    equipement_dict = json.load(f)
    for id_equipement in equipement_dict:
        disponibilite = equipement_dict[id_equipement]["DISPONIBILITE"]
        with orm.db_session:
            try:
                Equipement(id_equip=id_equipement, disponibilite=disponibilite)
                orm.commit()
            except:
                print(id_equipement, "already exists in database")
                pass
 
 
animal_data = 'TP-4/animal.json'
with open(animal_data, "r") as f:
    animal_dict = json.load(f)
    for id_animals in animal_dict:
        etat = animal_dict[id_animals]["ETAT"]
        type = animal_dict[id_animals]["TYPE"]
        race = animal_dict[id_animals]["RACE"]
        lieu = animal_dict[id_animals]["LIEU"]
        with orm.db_session:
            try:
                Animal(id_animal=id_animals,
                       etat=etat,
                       type=type,
                       race=race,
                       lieu=Equipement[lieu])
                orm.commit()
            except:
                print(id_animals, "already exists in database")
                pass