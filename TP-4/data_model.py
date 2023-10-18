from pony import orm

db = orm.Database()
 
class Equipement(db.Entity):
    id_equip = orm.PrimaryKey(str)
    disponibilite = orm.Required(str)
    animal = orm.Set("Animal")
 
class Animal(db.Entity):
    id_animal = orm.PrimaryKey(str)
    lieu = orm.Required(Equipement)
    etat = orm.Required(str)
    race = orm.Required(str)
    type = orm.Required(str)