import modele
import controleur

def test_lit_etat():
    assert modele.lit_etat('Tac') == 'affame'
def test_lit_etat_nul():
    assert modele.lit_etat('Bob') == None
def test_lit_lieu():
    assert modele.lit_lieu('Tac') == 'litiere'
def test_lit_lieu_nul():
    assert modele.lit_lieu('Bob') == None
def test_vérifie_disponibilité():
    assert modele.vérifie_disponibilité('litiere') == 'libre'
    assert modele.vérifie_disponibilité('nid') == 'occupe'



def test_cherche_occupant():
    assert modele.cherche_occupant('nid') == ['Pocahontas']
    assert 'Tac' in modele.cherche_occupant('litiere')
    assert 'Tac' not in modele.cherche_occupant('mangeoire')

def test_cherche_occupant_nul():
    assert modele.cherche_occupant('casino') == None

def test_change_état():
    modele.change_état('Totoro', 'fatigue')
    assert modele.lit_etat('Totoro') == 'fatigue'
    modele.change_état('Totoro', 'excité comme un pou')
    assert modele.lit_etat('Totoro') == 'fatigue'
    modele.change_état('Bob', 'fatigue')
    assert modele.lit_etat('Bob') == None

def test_change_lieu():
    modele.change_lieu('Totoro', 'roue')
    assert modele.lit_lieu('Totoro') == 'roue'
    assert modele.vérifie_disponibilité('litiere') == 'libre'
    assert modele.vérifie_disponibilité('roue') == 'occupe'

def test_change_lieu_occupe():
    modele.change_lieu('Totoro', 'nid')
    assert modele.lit_lieu('Totoro') == 'roue'

def test_change_lieu_nul_1():
    modele.change_lieu('Totoro', 'casino')
    assert modele.lit_lieu('Totoro') == 'roue'

import controleur 
 
def test_nourrir():
    if modele.vérifie_disponibilité('mangeoire') == 'libre' and modele.lit_etat('Tic') == 'affame':
        controleur.nourrir('Tic')
    assert modele.vérifie_disponibilité('mangeoire') == 'occupe'
    assert modele.lit_etat('Tic') == 'repus'
    assert modele.lit_lieu('Tic') == 'mangeoire'
    controleur.nourrir('Tac')
    assert modele.lit_etat('Tac') == 'affame'
    assert modele.lit_lieu('Tac') == 'litiere'
    controleur.nourrir('Pocahontas')
    assert modele.lit_etat('Pocahontas') == 'endormi'
    assert modele.lit_lieu('Pocahontas') == 'nid'
    controleur.nourrir('Bob')
    assert modele.lit_etat('Bob') == None
    assert modele.lit_lieu('Bob') == None
    assert modele.vérifie_disponibilité('mangeoire') == 'occupe'

test_change_lieu()
test_change_lieu_nul_1()

