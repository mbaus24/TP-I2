from appJar import gui
import modele
import controleur
app = gui()

app.addLabel("en-tête", "Bienvenue à l'animalerie!")
app.setLabelBg("en-tête", "salmon")
app.setLabelFg("en-tête", "white")

liste_animaux = ['Tic', 'Tac', 'Totoro', 'Patrick', 'Pocahontas']
liste_actions = ['nourrir','divertir','coucher','reveiller']


app.addLabel("tb", "Tableau de bord")
app.setLabelBg("tb", "grey")
app.setLabelFg("tb", "white")

k=0


for annimaux in liste_animaux:
    app.addLabel(annimaux, annimaux + ":" + modele.lit_etat(annimaux) + "," + modele.lit_lieu(annimaux))
    app.setLabelAlign(annimaux, "left")
    
    app.setLabelFg(annimaux, "black")
    if (k%2==0):
        app.setLabelBg(annimaux, "lavender")
    else:
        app.setLabelBg(annimaux, "pink")
    k=k+1

app.addLabel("la", "Liste des annimaux")
app.setLabelBg("la", "grey")
app.setLabelFg("la", "white")




for a in liste_animaux:
    app.addRadioButton("id_animal", a)

for c in liste_actions: 
    app.addRadioButton("action", c)

def maj():
    for annimaux in liste_animaux:
        app.setLabel(annimaux, annimaux + ":" + modele.lit_etat(annimaux) + "," + modele.lit_lieu(annimaux))

def press(act):

    if app.getRadioButton("action")=="nourrir":
        if(controleur.nourrir(app.getRadioButton("id_animal"))==1):
            app.warningBox("", "L'animal "+app.getRadioButton("id_animal")+" a été nourri")
        else:
            app.warningBox("", "Impossible pour le moment de nourrir l'animal "+app.getRadioButton("id_animal"))
    elif app.getRadioButton("action")=="divertir":
        if(controleur.divertir(app.getRadioButton("id_animal"))==1):
            app.warningBox("", "L'animal "+app.getRadioButton("id_animal")+" a été divertit")
        else:
            app.warningBox("", "Impossible pour le moment de divertir l'animal "+app.getRadioButton("id_animal"))
    elif app.getRadioButton("action")=="coucher":
        if(controleur.coucher(app.getRadioButton("id_animal"))==1):
            app.warningBox("", "L'animal "+app.getRadioButton("id_animal")+" a été couché")
        else:
            app.warningBox( "","Impossible pour le moment de coucher l'animal "+app.getRadioButton("id_animal"))
        
    elif app.getRadioButton("action")=="reveiller":
        if(controleur.reveiller(app.getRadioButton("id_animal"))==1):
            app.warningBox( "","L'animal "+app.getRadioButton("id_animal")+" a été réveillé")
        else:
            app.warningBox( "","Impossible pour le moment de réveiller l'animal "+app.getRadioButton("id_animal"))
    maj()
app.addButton("go",  press)






    
app.go()

