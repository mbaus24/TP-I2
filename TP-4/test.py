import modele

from data_model import orm, Equipement, Animal
 
def test_lit_etat():
    assert modele.lit_etat('Tac') == 'affame'
    assert modele.lit_etat('Bob') == None
 
@orm.db_session
def test_lit_lieu():
    assert modele.lit_lieu('Tac') == Equipement['litiere']
    assert modele.lit_lieu('Bob') == None
 
def test_verifie_disponibilite():
    assert modele.verifie_disponibilite('litiere') == 'libre'
    assert modele.verifie_disponibilite('roue') == 'libre'
    assert modele.verifie_disponibilite('nintendo') == None
 
@orm.db_session
def test_cherche_occupant():
    assert Animal['Totoro'] in modele.cherche_occupant('mangeoire')
    assert Animal['Tac'] in modele.cherche_occupant('litiere')
    assert Animal['Tac'] not in modele.cherche_occupant('mangeoire')
    assert modele.cherche_occupant('nintendo') == []
 
def test_change_etat():
    modele.change_etat('Totoro', 'fatigue')
    assert modele.lit_etat('Totoro') == 'fatigue'
    modele.change_etat('Totoro', 'excite comme un pou')
    assert modele.lit_etat('Totoro') == 'fatigue'
    modele.change_etat('Truc', 'fatigue')
    assert modele.lit_etat('Truc') == None
 
@orm.db_session
def test_change_lieu():
    modele.change_lieu('Totoro', 'roue')
    assert modele.lit_lieu('Totoro') == Equipement['roue']
    modele.change_lieu('Totoro', 'nid')
    assert modele.lit_lieu('Totoro') == Equipement['roue']
    modele.change_lieu('Totoro', 'nintendo')
    assert modele.lit_lieu('Totoro') == Equipement['roue']
    modele.change_lieu('Muche', 'litiere')
    assert modele.lit_lieu('Muche') == None
 
 
 
# @orm.db_session
# def test_nourrir():
#     if modele.verifie_disponibilite('mangeoire') == 'libre' and modele.lit_etat('Tic') == 'affame':
#         controleur.nourrir('Tic')
#     assert modele.verifie_disponibilite('mangeoire') == 'occupe'
#     assert modele.lit_etat('Tic') == 'repus'
#     assert modele.lit_lieu('Tic') == Equipement['mangeoire']
#     controleur.nourrir('Pocahontas')
#     assert modele.lit_etat('Pocahontas') == 'endormi'
#     assert modele.lit_lieu('Pocahontas') == Equipement['nid']
#     controleur.nourrir('Tac')
#     assert modele.lit_etat('Tac') == 'affame'
#     assert modele.lit_lieu('Tac') == Equipement['litiere']
#     controleur.nourrir('Bob')
#     assert modele.lit_etat('Bob') == None
#     assert modele.lit_lieu('Bob') == None
#     assert modele.verifie_disponibilite('mangeoire') == 'occupe'