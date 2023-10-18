import pandas


from pony import orm

db = orm.Database()
import numpy as np




with open("ventes_new.csv", encoding='utf-8') as f:
    data = pandas.read_csv(f)
print(data)


class Client(db.Entity):
    id_client = orm.PrimaryKey(str)
    telephone = orm.Required(str)
    ville = orm.Required(str)
    pays = orm.Required(str)
    achats = orm.Set('Commande')
    
class Produit(db.Entity):
    code_produit = orm.PrimaryKey(str)
    type_produit = orm.Required(str)
    prix_unitaire = orm.Required(float)
    ventes = orm.Set('Commande')
    
class Commande(db.Entity):
    num_commande = orm.Required(int)
    code_produit = orm.Required(str)
    orm.PrimaryKey(num_commande, code_produit)
    quantité = orm.Required(int)
    montant = orm.Required(float)
    mois = orm.Required(int)
    année = orm.Required(int)
    client = orm.Required(Client)
    produit = orm.Required(Produit)
    

db.bind(provider='sqlite', filename='ventes.db', create_db=True)
orm.set_sql_debug(True)
db.generate_mapping(create_tables=True)


produits = data[["CODE_PRODUIT", "TYPE_PRODUIT", "PRIX_UNITAIRE"]].drop_duplicates()
with orm.db_session:
    for p in produits.values:
        try:
            Produit(code_produit = p[0], type_produit = p[1], prix_unitaire = p[2])
            orm.commit()
        except Exception as e:
            print("*** ERREUR DE TRANSACTION :", e, '***')
            
            
Produit.select().show()