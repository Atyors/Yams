''' 
    Module d'interface du Yams

    @author: Romain Thieuw
'''

from modules.score import *
from modules.main import *
from os import *
from tkinter import *
from tkinter import messagebox
    


###=======================================
#Variables globales
fBo, tBo = ("Tahoma", 10, "bold"), 11 #Police d'écriture et largeur des bouton
tentatives = 2 # Nombre de relances disponibles
wCan, hCan = 455, 455 # Dimension du Canvas
turn = -1 # Tour des joueurs
played = 0 # Vérifie si le joueur a joué
nbJ = 2 # Nombre de joueurs
mode = 0
selection = [0, 0, 0, 0, 0] # Dés sélectionnés
last_selection = [0, 0, 0, 0, 0] # Sélection précédente
des_casses = [0, 0, 0, 0, 0]
current = "DodgerBlue4" # Couleur du joueur en cours

###=======================================
#Paramètrage des dés
x0, y0 = 90, 90
pt = 5


def absent():
    print("Cette section n'a pas encore été créée.")


###=======================================
#Gestion du jeu    
def un_joueur():
    global nbJ
    nbJ = 1
    Fscore_val1.pack(side=LEFT, padx=(10,85))
    Fscore_val2.forget()
    redem()


def deux_joueurs():
    global nbJ
    nbJ = 2
    Fscore_val1.pack(side=LEFT, padx=(10,0))
    Fscore_val2.pack(side=LEFT, padx=(15,5))
    redem()


def mode00():
    global mode
    mode = 0
    Bcasses.forget()
    redem()

def mode01():
    global mode
    mode = 1
    Bcasses.pack(side=BOTTOM)
    redem()


def redem():
    global turn, played, tentatives, selection, last_selection
    played, tentatives = 0, 2
    selection, last_selection = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
    if nbJ == 1:
        var_mode.set("Mode 1 joueur")
        turn = 0
    else:
        var_mode.set("Mode 2 joueurs")
        turn = -1
    if mode == 0:
        var_mode.set(var_mode.get() + " (NORMAL)")
    elif mode == 1:
        var_mode.set(var_mode.get() + " (DÉS CASSÉS)")
    var_J1_1.set("")
    var_J1_2.set("")
    var_J1_3.set("")
    var_J1_4.set("")
    var_J1_5.set("")
    var_J1_6.set("")
    var_J1_Bonus.set("")
    var_J1_TotalSup.set("")
    var_J1_Brelan.set("")
    var_J1_Carre.set("")
    var_J1_Full.set("")
    var_J1_Petite.set("")
    var_J1_Grande.set("")
    var_J1_Rien.set("")
    var_J1_Yams.set("")
    var_J1_Chance.set("")
    var_J1_TotalInf.set("")
    var_J1_Total.set("")
    var_J2_1.set("")
    var_J2_2.set("")
    var_J2_3.set("")
    var_J2_4.set("")
    var_J2_5.set("")
    var_J2_6.set("")
    var_J2_Bonus.set("")
    var_J2_TotalSup.set("")
    var_J2_Brelan.set("")
    var_J2_Carre.set("")
    var_J2_Full.set("")
    var_J2_Petite.set("")
    var_J2_Grande.set("")
    var_J2_Rien.set("")
    var_J2_Yams.set("")
    var_J2_Chance.set("")
    var_J2_TotalInf.set("")
    var_J2_Total.set("")
    button_off()
    can.delete(ALL)
    can.create_text(wCan/2, hCan/2, text="Joueur 1, lancez les dés.", font=("Tahoma", 25, "bold"), fill=current)
    can.create_text(wCan/2, hCan/2+50, text=var_mode.get(), font=("Tahoma", 15, "bold"), fill=current)
    Bjouer.config(state=NORMAL)
    Brelancer.config(state=DISABLED)
        

def relance_des():
    global des, des_casses, selection, tentatives, last_selection
    if selection != [0, 0, 0, 0, 0]:
        tentatives -= 1
        des = relance(selection, des, mode)
        des_casses = [0, 0, 0, 0, 0]
        if mode == 1:
            des, des_casses = des[0], des[1]
        if des_casses != [0, 0, 0, 0, 0]:
            Bcasses.config(state=NORMAL)
        else:
            Bcasses.config(state=DISABLED)
        last_selection = selection
        selection = [0, 0, 0, 0, 0]
        lancer()
    if tentatives == 0:
        Brelancer.config(state=DISABLED)


def relance_casses():
    global des, des_casses, selection, last_selection
    valide = 0
    for n in range(5):
        if des_casses[n] != 0 and selection[n] != 0:
            valide = 1
    if valide == 1:
        for n in range(5):
            if des_casses[n] != 0 and selection[n] != 0:
                des[n] = randint(1, 6)
        des_casses = [0, 0, 0, 0, 0]
        selection = [0, 0, 0, 0, 0]
        last_selection = [0, 0, 0, 0, 0]
        lancer()
        Bcasses.config(state=DISABLED)

    
def lancer():
    global tentatives, des, des_casses, played, turn
    if played == 0:
        des = jet_init(5, mode)
        if mode == 1:
            des, des_casses = des[0], des[1]
            if 1 in des_casses:
                Bcasses.config(state=NORMAL)
        dessine(des)
        played = 1
        Bjouer.config(state=DISABLED)
        Brelancer.config(state=NORMAL)
        if nbJ == 1:
            turn -= 2
        else:
            turn += 1
    can.delete(ALL)
    can.bind("<Button-1>", callback)
    can.create_text(wCan/2, hCan-50, text="Sélectionnez les dés que vous souhaitez relancer.", font=("Tahoma", 13, "bold"))
    dessine(des)
    outline_des()
    checking()
    if turn %2 == 0:
        joueur_courant()
        can.create_text(wCan/2, 30, text="Joueur 1", font=("Tahoma", 25, "bold"), fill=current)
    else:
        joueur_courant()
        can.create_text(wCan/2, 30, text="Joueur 2", font=("Tahoma", 25, "bold"), fill=current)


def button_off():
    Bun.config(state=DISABLED)
    Bdeux.config(state=DISABLED)
    Btrois.config(state=DISABLED)
    Bquatre.config(state=DISABLED)
    Bcinq.config(state=DISABLED)
    Bsix.config(state=DISABLED)
    Bbrelan.config(state=DISABLED)
    Bcarre.config(state=DISABLED)
    Bfull.config(state=DISABLED)
    Bpetite.config(state=DISABLED)
    Bgrande.config(state=DISABLED)
    Brien.config(state=DISABLED)
    Byams.config(state=DISABLED)
    Bchance.config(state=DISABLED)
        
def dessine(des):
    dessine_des()
    for n in range(len(des)):
        if des[n] == 1:
            dessine_1(n)
        if des[n] == 2:
            dessine_2(n)
        if des[n] == 3:
            dessine_3(n)
        if des[n] == 4:
            dessine_4(n)
        if des[n] == 5:
            dessine_5(n)
        if des[n] == 6:
            dessine_6(n)

def joueur_courant():
    global current
    if turn % 2 != 0:
        #Joueur 2
        LJ2.config(fg=current)
        LJ2_1.config(fg=current)
        LJ2_2.config(fg=current)
        LJ2_3.config(fg=current)
        LJ2_4.config(fg=current)
        LJ2_5.config(fg=current)
        LJ2_6.config(fg=current)
        LJ2_Bonus.config(fg=current)
        LJ2_TotSup.config(fg=current)
        LJ2_Brelan.config(fg=current)
        LJ2_Carre.config(fg=current)
        LJ2_Full.config(fg=current)
        LJ2_Petite.config(fg=current)
        LJ2_Grande.config(fg=current)
        LJ2_Rien.config(fg=current)
        LJ2_Yams.config(fg=current)
        LJ2_Chance.config(fg=current)
        LJ2_TotInf.config(fg=current)
        LJ2_Tot.config(fg=current)
        current = "black"
        #Joueur 1
        LJ1.config(fg=current)
        LJ1_1.config(fg=current)
        LJ1_2.config(fg=current)
        LJ1_3.config(fg=current)
        LJ1_4.config(fg=current)
        LJ1_5.config(fg=current)
        LJ1_6.config(fg=current)
        LJ1_Bonus.config(fg=current)
        LJ1_TotSup.config(fg=current)
        LJ1_Brelan.config(fg=current)
        LJ1_Carre.config(fg=current)
        LJ1_Full.config(fg=current)
        LJ1_Petite.config(fg=current)
        LJ1_Grande.config(fg=current)
        LJ1_Rien.config(fg=current)
        LJ1_Yams.config(fg=current)
        LJ1_Chance.config(fg=current)
        LJ1_TotInf.config(fg=current)
        LJ1_Tot.config(fg=current)
    elif turn % 2 == 0:
        #Joueur 1
        LJ1.config(fg=current)
        LJ1_1.config(fg=current)
        LJ1_2.config(fg=current)
        LJ1_3.config(fg=current)
        LJ1_4.config(fg=current)
        LJ1_5.config(fg=current)
        LJ1_6.config(fg=current)
        LJ1_Bonus.config(fg=current)
        LJ1_TotSup.config(fg=current)
        LJ1_Brelan.config(fg=current)
        LJ1_Carre.config(fg=current)
        LJ1_Full.config(fg=current)
        LJ1_Petite.config(fg=current)
        LJ1_Grande.config(fg=current)
        LJ1_Rien.config(fg=current)
        LJ1_Yams.config(fg=current)
        LJ1_Chance.config(fg=current)
        LJ1_TotInf.config(fg=current)
        LJ1_Tot.config(fg=current)
        current = "black"
        #Joueur 2
        LJ2.config(fg=current)
        LJ2_1.config(fg=current)
        LJ2_2.config(fg=current)
        LJ2_3.config(fg=current)
        LJ2_4.config(fg=current)
        LJ2_5.config(fg=current)
        LJ2_6.config(fg=current)
        LJ2_Bonus.config(fg=current)
        LJ2_TotSup.config(fg=current)
        LJ2_Brelan.config(fg=current)
        LJ2_Carre.config(fg=current)
        LJ2_Full.config(fg=current)
        LJ2_Petite.config(fg=current)
        LJ2_Grande.config(fg=current)
        LJ2_Rien.config(fg=current)
        LJ2_Yams.config(fg=current)
        LJ2_Chance.config(fg=current)
        LJ2_TotInf.config(fg=current)
        LJ2_Tot.config(fg=current)
    current= "DodgerBlue4"
    


###=======================================
#Fonctions d'interface
def chg_tour():
    global turn, tentatives, selection, last_selection
    if played == 0:
        selection, last_selection = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
        add_bonus()
        add_total()
        tentatives = 2
        can.unbind("<Button-1>")
        Bjouer.config(state=NORMAL)
        Brelancer.config(state=DISABLED)
        Bcasses.config(state=DISABLED)
        button_off()
        can.delete(ALL)
        if turn %2 == 0 and nbJ != 1:
            joueur_courant()
            can.create_text(wCan/2, hCan/2, text="Joueur 2, lancez les dés.", font=("Tahoma", 25, "bold"), fill=current)
        else:
            joueur_courant()
            can.create_text(wCan/2, hCan/2, text="Joueur 1, lancez les dés.", font=("Tahoma", 25, "bold"), fill=current)
    if turn == 27 or turn == -28:
        can.delete(ALL)
        Bjouer.config(state=DISABLED)
        if nbJ == 1:
            can.create_text(wCan/2, hCan/2, text="La partie est terminée !\nVous avez fait : "+var_J1_Total.get(), font=("Tahoma", 25, "bold"))
        else:
            if int(var_J1_Total.get()) > int(var_J2_Total.get()):
                can.create_text(wCan/2, hCan/2, text="Le joueur 1 a gagné !", font=("Tahoma", 25, "bold"))
            elif int(var_J1_Total.get()) < int(var_J2_Total.get()):
                can.create_text(wCan/2, hCan/2, text="Le joueur 2 a gagné !", font=("Tahoma", 25, "bold"))
            else:
                can.create_text(wCan/2, hCan/2, text="On dirait qu'on a\n une égalité ici !", font=("Tahoma", 25, "bold"))
        
                        

def add_un():
    global played
    if turn % 2 == 0 and played == 1:
        val = var_J1_1.get()
        if val == "":
            var_J1_1.set(un(des))
            played = 0
    elif turn % 2 != 0 and played == 1:
        val = var_J2_1.get()
        if val == "":
            var_J2_1.set(un(des))
            played = 0
    chg_tour()
    

def add_deux():
    global played
    if turn % 2 == 0 and played == 1:
        val = var_J1_2.get()
        if val == "":
            var_J1_2.set(deux(des))
            played = 0
    elif turn % 2 != 0 and played == 1:
        val = var_J2_2.get()
        if val == "":
            var_J2_2.set(deux(des))
            played = 0
    chg_tour()

def add_trois():
    global played
    if turn % 2 == 0 and played == 1:
        val = var_J1_3.get()
        if val == "":
            var_J1_3.set(trois(des))
            played = 0
    elif turn % 2 != 0 and played == 1:
        val = var_J2_3.get()
        if val == "":
            var_J2_3.set(trois(des))
            played = 0
    chg_tour()


def add_quatre():
    global played
    if turn % 2 == 0 and played == 1:
        val = var_J1_4.get()
        if val == "":
            var_J1_4.set(quatre(des))
            played = 0
    elif turn % 2 != 0 and played == 1:
        val = var_J2_4.get()
        if val == "":
            var_J2_4.set(quatre(des))
            played = 0
    chg_tour()


def add_cinq():
    global played
    if turn % 2 == 0 and played == 1:
        val = var_J1_5.get()
        if val == "":
            var_J1_5.set(cinq(des))
            played = 0
    elif turn % 2 != 0 and played == 1:
        val = var_J2_5.get()
        if val == "":
            var_J2_5.set(cinq(des))
            played = 0
    chg_tour()


def add_six():
    global played
    if turn % 2 == 0 and played == 1:
        val = var_J1_6.get()
        if val == "":
            var_J1_6.set(six(des))
            played = 0
    elif turn % 2 != 0 and played == 1:
        val = var_J2_6.get()
        if val == "":
            var_J2_6.set(six(des))
            played = 0
    chg_tour()


def add_bonus():
    somme = 0
    if turn % 2 == 0:
        score = [var_J1_1.get(), var_J1_2.get(), var_J1_3.get(), var_J1_4.get(), var_J1_5.get(), var_J1_6.get()]
        for elem in score:
            if elem != "":
                somme += int(elem)
                if bonus(somme):
                    var_J1_Bonus.set(35)
                    var_J1_TotalSup.set(somme + 35)
                else:
                    var_J1_TotalSup.set(somme)
    if turn % 2 != 0:
        score = [var_J2_1.get(), var_J2_2.get(), var_J2_3.get(), var_J2_4.get(), var_J2_5.get(), var_J2_6.get()]
        for elem in score:
            if elem != "":
                somme += int(elem)
                if bonus(somme):
                    var_J2_Bonus.set(35)
                    var_J2_TotalSup.set(somme + 35)
                else:
                    var_J2_TotalSup.set(somme)
                    

def add_brelan():
    global played
    if turn % 2 == 0 and played == 1:
        if brelan(des) and var_J1_Brelan.get() == "":
            var_J1_Brelan.set(brelan(des))
            played = 0
        else:
            choix = messagebox.askquestion("Continuer ?", "Vos dés ne permettent pas d'effectuer cette valeur,\nêtes-vous sûr de vouloir y mettre 0 ?")
            if choix == "yes":
                var_J1_Brelan.set(0)
                played = 0
    elif turn % 2 != 0 and played == 1:
        if brelan(des) and var_J2_Brelan.get() == "":
            var_J2_Brelan.set(brelan(des))
            played = 0
        else:
            choix = messagebox.askquestion("Continuer ?", "Vos dés ne permettent pas d'effectuer cette valeur,\nêtes-vous sûr de vouloir y mettre 0 ?")
            if choix == "yes":
                var_J2_Brelan.set(0)
                played = 0
    chg_tour()


def add_carre():
    global played
    if turn % 2 == 0 and played == 1:
        if carre(des) and var_J1_Carre.get() == "":
            var_J1_Carre.set(carre(des))
            played = 0
        else:
            choix = messagebox.askquestion("Continuer ?", "Vos dés ne permettent pas d'effectuer cette valeur,\nêtes-vous sûr de vouloir y mettre 0 ?")
            if choix == "yes":
                var_J1_Carre.set(0)
                played = 0
    elif turn % 2 != 0 and played == 1:
        if carre(des) and var_J2_Carre.get() == "":
            var_J2_Carre.set(carre(des))
            played = 0
        else:
            choix = messagebox.askquestion("Continuer ?", "Vos dés ne permettent pas d'effectuer cette valeur,\nêtes-vous sûr de vouloir y mettre 0 ?")
            if choix == "yes":
                var_J2_Carre.set(0)
                played = 0
    chg_tour()


def add_full():
    global played
    if turn % 2 == 0 and played == 1:
        if full(des) and var_J1_Full.get() == "":
            var_J1_Full.set(full(des))
            played = 0
        else:
            choix = messagebox.askquestion("Continuer ?", "Vos dés ne permettent pas d'effectuer cette valeur,\nêtes-vous sûr de vouloir y mettre 0 ?")
            if choix == "yes":
                var_J1_Full.set(0)
                played = 0
    elif turn % 2 != 0 and played == 1:
        if full(des) and var_J2_Full.get() == "":
            var_J2_Full.set(full(des))
            played = 0
        else:
            choix = messagebox.askquestion("Continuer ?", "Vos dés ne permettent pas d'effectuer cette valeur,\nêtes-vous sûr de vouloir y mettre 0 ?")
            if choix == "yes":
                var_J2_Full.set(0)
                played = 0
    chg_tour()

    
def add_petite():
    global played
    if turn % 2 == 0 and played == 1:
        if petite(des) and var_J1_Petite.get() == "":
            var_J1_Petite.set(petite(des))
            played = 0
        else:
            choix = messagebox.askquestion("Continuer ?", "Vos dés ne permettent pas d'effectuer cette valeur,\nêtes-vous sûr de vouloir y mettre 0 ?")
            if choix == "yes":
                var_J1_Petite.set(0)
                played = 0
    elif turn % 2 != 0 and played == 1:
        if petite(des) and var_J2_Petite.get() == "":
            var_J2_Petite.set(petite(des))
            played = 0
        else:
            choix = messagebox.askquestion("Continuer ?", "Vos dés ne permettent pas d'effectuer cette valeur,\nêtes-vous sûr de vouloir y mettre 0 ?")
            if choix == "yes":
                var_J2_Petite.set(0)
                played = 0
    chg_tour()


def add_grande():
    global played
    if turn % 2 == 0 and played == 1:
        if grande(des) and var_J1_Grande.get() == "":
            var_J1_Grande.set(grande(des))
            played = 0
        else:
            choix = messagebox.askquestion("Continuer ?", "Vos dés ne permettent pas d'effectuer cette valeur,\nêtes-vous sûr de vouloir y mettre 0 ?")
            if choix == "yes":
                var_J1_Grande.set(0)
                played = 0
    elif turn % 2 != 0 and played == 1:
        if grande(des) and var_J2_Grande.get() == "":
            var_J2_Grande.set(grande(des))
            played = 0
        else:
            choix = messagebox.askquestion("Continuer ?", "Vos dés ne permettent pas d'effectuer cette valeur,\nêtes-vous sûr de vouloir y mettre 0 ?")
            if choix == "yes":
                var_J2_Grande.set(0)
                played = 0
    chg_tour()


def add_rien():
    global played
    if turn % 2 == 0 and played == 1:
        if rien(des) and var_J1_Rien.get() == "":
            var_J1_Rien.set(rien(des))
            played = 0
        else:
            choix = messagebox.askquestion("Continuer ?", "Vos dés ne permettent pas d'effectuer cette valeur,\nêtes-vous sûr de vouloir y mettre 0 ?")
            if choix == "yes":
                var_J1_Rien.set(0)
                played = 0
    elif turn % 2 != 0 and played == 1:
        if rien(des) and var_J2_Rien.get() == "":
            var_J2_Rien.set(rien(des))
            played = 0
        else:
            choix = messagebox.askquestion("Continuer ?", "Vos dés ne permettent pas d'effectuer cette valeur,\nêtes-vous sûr de vouloir y mettre 0 ?")
            if choix == "yes":
                var_J2_Rien.set(0)
                played = 0
    chg_tour()


def add_yams():
    global played
    if turn % 2 == 0 and played == 1:
        if yams(des) and var_J1_Yams.get() == "":
            var_J1_Yams.set(yams(des))
            played = 0
        else:
            choix = messagebox.askquestion("Continuer ?", "Vos dés ne permettent pas d'effectuer cette valeur,\nêtes-vous sûr de vouloir y mettre 0 ?")
            if choix == "yes":
                var_J1_Yams.set(0)
                played = 0
    elif turn % 2 != 0 and played == 1:
        if yams(des) and var_J2_Yams.get() == "":
            var_J2_Yams.set(yams(des))
            played = 0
        else:
            choix = messagebox.askquestion("Continuer ?", "Vos dés ne permettent pas d'effectuer cette valeur,\nêtes-vous sûr de vouloir y mettre 0 ?")
            if choix == "yes":
                var_J2_Yams.set(0)
                played = 0
    chg_tour()


def add_chance():
    global played
    if turn % 2 == 0 and played == 1:
        if var_J1_Chance.get() == "":
            var_J1_Chance.set(chance(des))
            played = 0
    elif turn % 2 != 0 and played == 1:
        if var_J2_Chance.get() == "":
            var_J2_Chance.set(chance(des))
            played = 0
    chg_tour()   


def add_total():
    somme = 0
    if turn % 2 == 0:
        score = [var_J1_Brelan.get(), var_J1_Carre.get(), var_J1_Full.get(), var_J1_Petite.get(), var_J1_Grande.get(), var_J1_Yams.get(), var_J1_Chance.get()]
        for elem in score:
            if elem != "":
                somme += int(elem)
        var_J1_TotalInf.set(somme)
        if var_J1_TotalSup.get() != "":
            var_J1_Total.set(int(var_J1_TotalSup.get()) + int(var_J1_TotalInf.get()))
        else:
            var_J1_Total.set(var_J1_TotalInf.get())
    if turn % 2 != 0:
        score = [var_J2_Brelan.get(), var_J2_Carre.get(), var_J2_Full.get(), var_J2_Petite.get(), var_J2_Grande.get(), var_J2_Yams.get(), var_J2_Chance.get()]
        for elem in score:
            if elem != "":
                somme += int(elem)
        var_J2_TotalInf.set(somme)
        if var_J2_TotalSup.get() != "":
            var_J2_Total.set(int(var_J2_TotalSup.get()) + int(var_J2_TotalInf.get()))
        else:
            var_J2_Total.set(var_J2_TotalInf.get())
                

###=======================================
#Dessins des points sur les dés
col_des = "saddle brown" #couleur des dés
col_pt = "light goldenrod" #couleur des point


def dessine_des():
    for pos in range(5):
        if pos <= 2:
            can.create_rectangle(x0*pos + (wCan/10)*(pos + 1), y0, x0*pos + x0 + (wCan/10)*(pos + 1), y0*2, fill=col_des)
        else:
            pos -= 3
            can.create_rectangle(x0*pos + (wCan/5)*(pos + 1), y0*2.5, x0*pos + x0 + (wCan/5)*(pos + 1), y0*3.5, fill=col_des)

def dessine_1(pos):
    if pos <= 2:
        can.create_oval(x0*pos + (wCan/10)*(pos + 1) + 1/3*x0 + pt, y0 + 1/3*y0 + pt, x0*pos + x0 + (wCan/10)*(pos + 1) - 1/3*x0 - pt, y0*2 - 1/3*y0 -pt, fill=col_pt) #Point central
    if pos == 3 or pos == 4:
        pos -= 3
        can.create_oval(x0*pos + (wCan/5)*(pos + 1) + 1/3*x0 + pt, y0*2.5 + 1/3*y0 + pt, x0*pos + x0 + (wCan/5)*(pos + 1) - 1/3*x0 - pt, y0*3.5 - 1/3*y0 - pt, fill=col_pt) #Point central

def dessine_2(pos):
    if pos <= 2:
        can.create_oval(x0*pos + (wCan/10)*(pos + 1) + 2/3*x0 + pt, y0 + pt, x0*pos + x0 + (wCan/10)*(pos + 1) - pt, y0*2 - 2/3*y0 - pt, fill=col_pt) #Point NE
        can.create_oval(x0*pos + (wCan/10)*(pos + 1) + pt, y0 + 2/3*y0 + pt, x0*pos + x0 + (wCan/10)*(pos + 1) - 2/3*x0 - pt, y0*2 - pt, fill=col_pt) #Point SW
    if pos == 3 or pos == 4:
        pos -= 3
        can.create_oval(x0*pos + (wCan/5)*(pos + 1) + 2/3*x0 + pt, y0*2.5 + pt, x0*pos + x0 + (wCan/5)*(pos + 1) - pt, y0*3.5 - 2/3*y0 - pt, fill=col_pt) #Point NE
        can.create_oval(x0*pos + (wCan/5)*(pos + 1) + pt, y0*2.5 + 2/3*y0 + pt, x0*pos + x0 + (wCan/5)*(pos + 1) - 2/3*x0 - pt, y0*3.5 - pt, fill=col_pt) #Point SW

def dessine_3(pos):
    dessine_1(pos)
    dessine_2(pos)

def dessine_4(pos):
    dessine_2(pos)
    if pos <= 2:
        can.create_oval(x0*pos + (wCan/10)*(pos + 1) + pt, y0 + pt, x0*pos + x0 + (wCan/10)*(pos + 1) - 2/3*x0 - pt, y0*2 - 2/3*y0 - pt, fill=col_pt) #Point NW
        can.create_oval(x0*pos + (wCan/10)*(pos + 1) + 2/3*x0 + pt, y0 + 2/3*y0 + pt, x0*pos + x0 + (wCan/10)*(pos + 1) - pt, y0*2 - pt, fill=col_pt) #Point SE
    if pos == 3 or pos == 4:
        pos -= 3
        can.create_oval(x0*pos + (wCan/5)*(pos + 1) + pt, y0*2.5 + pt, x0*pos + x0 + (wCan/5)*(pos + 1) - 2/3*x0 - pt, y0*3.5 - 2/3*y0 - pt, fill=col_pt) #Point NW
        can.create_oval(x0*pos + (wCan/5)*(pos + 1) + 2/3*x0 + pt, y0*2.5 + 2/3*y0 + pt, x0*pos + x0 + (wCan/5)*(pos + 1) - pt, y0*3.5 - pt, fill=col_pt) #Point SE

def dessine_5(pos):
    dessine_4(pos)
    dessine_1(pos)

def dessine_6(pos):
    dessine_4(pos)
    if pos <= 2:
        can.create_oval(x0*pos + (wCan/10)*(pos + 1) + pt, y0 + 1/3*y0 + pt, x0*pos + x0 + (wCan/10)*(pos + 1) - 2/3*x0 - pt, y0*2 - 1/3*y0 - pt, fill=col_pt) #Point W
        can.create_oval(x0*pos + (wCan/10)*(pos + 1) + 2/3*x0 + pt, y0 + 1/3*y0 + pt, x0*pos + x0 + (wCan/10)*(pos + 1) - pt, y0*2 - 1/3*y0 - pt, fill=col_pt) #Point E
    if pos == 3 or pos == 4:
        pos -= 3
        can.create_oval(x0*pos + (wCan/5)*(pos + 1) + 2/3*x0 + pt, y0*2.5 + 1/3*y0 + pt, x0*pos + x0 + (wCan/5)*(pos + 1) - pt, y0*3.5 - 1/3*y0 - pt, fill=col_pt) #Point W
        can.create_oval(x0*pos + (wCan/5)*(pos + 1) + pt, y0*2.5 + 1/3*y0 + pt, x0*pos + x0 + (wCan/5)*(pos + 1) - 2/3*x0 - pt, y0*3.5 - 1/3*y0 - pt, fill=col_pt) #Point NE


###=======================================
#Gestion des cliques sur le Canvas
col_outline = "dark goldenrod"
col_outline_last = "firebrick3"
col_outline_casse = "green"
def callback(event):
    """Récupère les coordonnées des clics.
    """
    global selection
    X, Y = event.x, event.y
    if (46 <= X <= 136) and (90 <= Y <= 180):
        if selection [0] == (0, des[0]):
            selection [0] = 0
            lancer()
        else:
            selection[0] = (0, des[0])
    if (181 <= X <= 271) and (90 <= Y <= 180):
        if selection [1] == (1, des[1]):
            selection [1] = 0
            lancer()
        else:
            selection[1] = (1, des[1])
    if (316 <= X <= 406) and (90 <= Y <= 180):
        if selection [2] == (2, des[2]):
            selection [2] = 0
            lancer()
        else:
            selection[2] = (2, des[2])
    if (91 <= X <= 181) and (225 <= Y <= 315):
        if selection [3] == (3, des[3]):
            selection [3] = 0
            lancer()
        else:
            selection[3] = (3, des[3])
    if (272 <= X <= 362) and (225 <= Y <= 315):
        if selection [4] == (4, des[4]):
            selection [4] = 0
            lancer()
        else:
            selection[4] = (4, des[4])
    outline_des()


def outline_des():
    t = 6
    if selection[0] == (0, des[0]):
        can.create_rectangle(46, 90, 136, 180, outline=col_outline, width=t)
    if des_casses[0] != 0:
        can.create_line(46, 190, 136, 190, fill=col_outline_casse, width=t*2.5)
        can.create_text(91, 190, text="Cassé")
    elif last_selection[0] != 0:
        can.create_line(46, 190, 136, 190, fill=col_outline_last, width=t*2.5)
        can.create_text(91, 190, text="Relancé")

    if selection[1] == (1, des[1]):
        can.create_rectangle(181, 90, 271, 180, outline=col_outline, width=t)
    if des_casses[1] != 0:
        can.create_line(181, 190, 271, 190, fill=col_outline_casse, width=t*2.5)
        can.create_text(226, 190, text="Cassé")
    elif last_selection[1] != 0:
        can.create_line(181, 190, 271, 190, fill=col_outline_last, width=t*2.5)
        can.create_text(226, 190, text="Relancé")

    if selection[2] == (2, des[2]):
        can.create_rectangle(316, 90, 406, 180, outline=col_outline, width=t)
    if des_casses[2] != 0:
        can.create_line(316, 190, 406, 190, fill=col_outline_casse, width=t*2.5)
        can.create_text(361, 190, text="Cassé")
    elif last_selection[2] != 0:
        can.create_line(316, 190, 406, 190, fill=col_outline_last, width=t*2.5)
        can.create_text(361, 190, text="Relancé")

    if selection[3] == (3, des[3]):
        can.create_rectangle(91, 225, 181, 315, outline=col_outline, width=t)
    if des_casses[3] != 0:
        can.create_line(91, 325, 181, 325, fill=col_outline_casse, width=t*2.5)
        can.create_text(136, 325, text="Cassé")
    elif last_selection[3] != 0:
        can.create_line(91, 325, 181, 325, fill=col_outline_last, width=t*2.5)
        can.create_text(136, 325, text="Relancé")

    if selection[4] == (4, des[4]):
        can.create_rectangle(272, 225, 362, 315, outline=col_outline, width=t)
    if des_casses[4] != 0:
        can.create_line(272, 325, 362, 325, fill=col_outline_casse, width=t*2.5)
        can.create_text(317, 325, text="Cassé")
    elif last_selection[4] != 0:
        can.create_line(272, 325, 362, 325, fill=col_outline_last, width=t*2.5)
        can.create_text(317, 325, text="Relancé")

        
def checking():
    if turn % 2 == 0:
        if var_J1_1.get() != "": Bun.config(state=DISABLED)
        else: Bun.config(state=NORMAL)
        if var_J1_2.get() != "": Bdeux.config(state=DISABLED)
        else: Bdeux.config(state=NORMAL)
        if var_J1_3.get() != "": Btrois.config(state=DISABLED)
        else: Btrois.config(state=NORMAL)
        if var_J1_4.get() != "": Bquatre.config(state=DISABLED)
        else: Bquatre.config(state=NORMAL)
        if var_J1_5.get() != "": Bcinq.config(state=DISABLED)
        else: Bcinq.config(state=NORMAL)
        if var_J1_6.get() != "": Bsix.config(state=DISABLED)
        else: Bsix.config(state=NORMAL)
        if var_J1_Brelan.get() != "": Bbrelan.config(state=DISABLED)
        else: Bbrelan.config(state=NORMAL)
        if var_J1_Carre.get() != "": Bcarre.config(state=DISABLED)
        else: Bcarre.config(state=NORMAL)
        if var_J1_Full.get() != "": Bfull.config(state=DISABLED)
        else: Bfull.config(state=NORMAL)
        if var_J1_Petite.get() != "": Bpetite.config(state=DISABLED)
        else: Bpetite.config(state=NORMAL)
        if var_J1_Grande.get() != "": Bgrande.config(state=DISABLED)
        else: Bgrande.config(state=NORMAL)
        if var_J1_Rien.get() != "": Brien.config(state=DISABLED)
        else: Brien.config(state=NORMAL)
        if var_J1_Yams.get() != "": Byams.config(state=DISABLED)
        else: Byams.config(state=NORMAL)
        if var_J1_Chance.get() != "": Bchance.config(state=DISABLED)
        else: Bchance.config(state=NORMAL)
    elif turn % 2 != 0:
        if var_J2_1.get() != "": Bun.config(state=DISABLED)
        else: Bun.config(state=NORMAL)
        if var_J2_2.get() != "": Bdeux.config(state=DISABLED)
        else: Bdeux.config(state=NORMAL)
        if var_J2_3.get() != "": Btrois.config(state=DISABLED)
        else: Btrois.config(state=NORMAL)
        if var_J2_4.get() != "": Bquatre.config(state=DISABLED)
        else: Bquatre.config(state=NORMAL)
        if var_J2_5.get() != "": Bcinq.config(state=DISABLED)
        else: Bcinq.config(state=NORMAL)
        if var_J2_6.get() != "": Bsix.config(state=DISABLED)
        else: Bsix.config(state=NORMAL)
        if var_J2_Brelan.get() != "": Bbrelan.config(state=DISABLED)
        else: Bbrelan.config(state=NORMAL)
        if var_J2_Carre.get() != "": Bcarre.config(state=DISABLED)
        else: Bcarre.config(state=NORMAL)
        if var_J2_Full.get() != "": Bfull.config(state=DISABLED)
        else: Bfull.config(state=NORMAL)
        if var_J2_Petite.get() != "": Bpetite.config(state=DISABLED)
        else: Bpetite.config(state=NORMAL)
        if var_J2_Grande.get() != "": Bgrande.config(state=DISABLED)
        else: Bgrande.config(state=NORMAL)
        if var_J2_Rien.get() != "": Brien.config(state=DISABLED)
        else: Brien.config(state=NORMAL)
        if var_J2_Yams.get() != "": Byams.config(state=DISABLED)
        else: Byams.config(state=NORMAL)
        if var_J2_Chance.get() != "": Bchance.config(state=DISABLED)
        else: Bchance.config(state=NORMAL)

         
###=======================================
#Ouverture de la fenêtre
###=======================================
fenetre = Tk()

fenetre.title("Yams !")

menubar = Menu(fenetre)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Nouvelle partie", command=redem)
menu1.add_separator()
menu1.add_command(label="Un joueur", command=un_joueur)
menu1.add_command(label="Deux joueurs", command=deux_joueurs)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.destroy)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Mode Normal", command=mode00)
menu2.add_command(label="Mode Dés cassés", command=mode01)
menubar.add_cascade(label="Options", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="Règles du jeu", command=absent)
menu3.add_command(label="Informations", command=absent)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu = menubar, bg="grey7")
###=======================================
#Widgets
###=======================================
#Représentation des dés
fen = Frame(fenetre)
fen.pack()

Fhaut = Frame(fen)
Fhaut.pack(side=TOP)

Fbas = Frame(fen)
Fbas.pack(side=BOTTOM)

can = Canvas(Fhaut, width=wCan, height=hCan, bg="grey60", bd=-3)
can.pack(side=LEFT)

can.create_text(wCan/2, hCan/2, text="Joueur 1, lancez les dés.", font=("Tahoma", 25, "bold"), fill=current)


###=======================================
#Boutons de sélections
Fbout = Frame(Fbas)
Fbout.pack(side=LEFT)
Fline_1 = Frame(Fbout)
Fline_2 = Frame(Fbout)
Fline_3 = Frame(Fbout)
Fline_4 = Frame(Fbout)

#Partie supérieure
Bun = Button(Fline_1, text="AS", command=add_un, font=fBo, width=tBo)
Bdeux = Button(Fline_2, text="DEUX", command=add_deux, font=fBo, width=tBo)
Btrois = Button(Fline_3, text="TROIS", command=add_trois, font=fBo, width=tBo)
Bquatre = Button(Fline_1, text="QUATRE", command=add_quatre, font=fBo, width=tBo)
Bcinq = Button(Fline_2, text="CINQ", command=add_cinq, font=fBo, width=tBo)
Bsix = Button(Fline_3, text="SIX", command=add_six, font=fBo, width=tBo)

#Partie inférieure
Bbrelan = Button(Fline_1, text="BRELAN", command=add_brelan, font=fBo, width=tBo)
Bcarre = Button(Fline_2, text="CARRE", command=add_carre, font=fBo, width=tBo)
Bfull = Button(Fline_3, text="FULL", command=add_full, font=fBo, width=tBo)
Bpetite = Button(Fline_1, text="PETITE SUITE", command=add_petite, font=fBo, width=tBo)
Bgrande= Button(Fline_2, text="GRANDE SUITE", command=add_grande, font=fBo, width=tBo)
Brien= Button(Fline_2, text="RIEN", command=add_rien, font=fBo, width=tBo)
Byams = Button(Fline_3, text="YAMS", command=add_yams, font=fBo, width=tBo)
Bchance = Button(Fbout, text="CHANCE", command=add_chance, font=fBo, width=tBo)


###=======================================
#Packing Frame des boutons
Fline_1.pack(side=TOP)
Fline_2.pack(side=TOP)
Fline_3.pack(side=TOP)
Bchance.pack(side=BOTTOM)

###=======================================
#Packing des boutons
Bun.pack(side=LEFT)
Bdeux.pack(side=LEFT)
Btrois.pack(side=LEFT)
Bquatre.pack(side=LEFT)
Bcinq.pack(side=LEFT)
Bsix.pack(side=LEFT)
Bbrelan.pack(side=LEFT)
Bcarre.pack(side=LEFT)
Bfull.pack(side=LEFT)
Bpetite.pack(side=LEFT)
Bgrande.pack(side=LEFT)
Brien.pack(side=LEFT)
Byams.pack(side=LEFT)
Bchance.pack()

###=======================================
#Lancer les dés et quitter le jeu
Fmenu = Frame(Fbas)
Fjouer = Frame(Fmenu)
FmenuB = Frame(Fmenu)

Fmenu.pack(side=RIGHT, padx=(50,0))
FmenuB.pack(side=BOTTOM)
Fjouer.pack(side=TOP)

var_mode = StringVar()
var_mode.set("Mode 2 joueurs (NORMAL)")

Flabel = Frame(Fjouer)
Flabel.grid(row=0, column=0, columnspan=2)
Label(Flabel, textvariable=var_mode, font=fBo).pack()
Bjouer = Button(Fjouer, text="LANCER LES DÉS", command=lancer, font=fBo, width=15)
Bjouer.grid(row=1, column=0)
Brelancer = Button(Fjouer, text="RELANCER LES DÉS", command=relance_des, font=fBo, width=15)
Brelancer.grid(row=1, column=1)
Brelancer.config(state=DISABLED)

Fcasses = Frame(Fjouer)
Fcasses.grid(row=2, column=0, columnspan=2)
Bcasses = Button(Fcasses, text="RELANCER LES DÉS CASSÉS", command=relance_casses, font=fBo, width=22)
Bcasses.config(state=DISABLED)

###=======================================
#Valeur des scores
Fparam = Frame(Fhaut)
Fparam.pack()
Fscore_val = Frame(Fparam)
Fscore_val.pack(side=LEFT)
font_score = ("Tahoma", 10, "bold")

Tscore = 14
Label(Fscore_val, text="", font=fBo).pack()
Label(Fscore_val, text="AS :", font=font_score, width=Tscore, anchor=E).pack()
Label(Fscore_val, text="DEUX :", font=font_score, width=Tscore, anchor=E).pack()
Label(Fscore_val, text="TROIS :", font=font_score, width=Tscore, anchor=E).pack()
Label(Fscore_val, text="QUATRE :", font=font_score, width=Tscore, anchor=E).pack()
Label(Fscore_val, text="CINQ :", font=font_score, width=Tscore, anchor=E).pack()
Label(Fscore_val, text="SIX :", font=font_score, width=Tscore, anchor=E).pack()
Label(Fscore_val, text="BONUS :", font=font_score, width=Tscore, anchor=E).pack()
Label(Fscore_val, text="TOTAL :", font=font_score, width=Tscore, anchor=E).pack()
Label(Fscore_val, text="", font=font_score).pack()
Label(Fscore_val, text="", font=font_score).pack()
Label(Fscore_val, text="BRELAN :", font=font_score, width=Tscore, anchor=E).pack()
Label(Fscore_val, text="CARRE :", font=font_score, width=Tscore, anchor=E).pack()
Label(Fscore_val, text="FULL :", font=font_score, width=Tscore, anchor=E).pack()
Label(Fscore_val, text="PETITE SUITE :", font=font_score, width=Tscore, anchor=E).pack()
Label(Fscore_val, text="GRANDE SUITE :", font=font_score, width=Tscore, anchor=E).pack()
Label(Fscore_val, text="RIEN :", font=font_score, width=Tscore, anchor=E).pack()
Label(Fscore_val, text="YAMS :", font=font_score, width=Tscore, anchor=E).pack()
Label(Fscore_val, text="CHANCE :", font=font_score, width=Tscore, anchor=E).pack()
Label(Fscore_val, text="TOTAL :", font=font_score, width=Tscore, anchor=E).pack()
Label(Fscore_val, text="", font=font_score).pack()
Label(Fscore_val, text="SCORE FINAL :", font=font_score, width=Tscore, anchor=E).pack()


###=======================================
#Joueurs
###=======================================
Fscore_val1 = Frame(Fparam)
Fscore_val1.pack(side=LEFT, padx=(10,0))

LJ1 = Label(Fscore_val1, text="JOUEUR 1", font=fBo, fg=current)
LJ1.pack()
#Variables de score du joueur 1
var_J1_1, var_J1_2, var_J1_3, var_J1_4 = StringVar(), StringVar(), StringVar(), StringVar()
var_J1_5, var_J1_6, var_J1_Bonus, var_J1_TotalSup = StringVar(), StringVar(), StringVar(), StringVar()
var_J1_Brelan, var_J1_Carre, var_J1_Full, var_J1_Petite = StringVar(), StringVar(), StringVar(), StringVar()
var_J1_Grande, var_J1_Rien, var_J1_Yams, var_J1_Chance, var_J1_TotalInf = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
var_J1_Total =StringVar()

LJ1_1 = Label(Fscore_val1, textvariable=var_J1_1, font=font_score)
LJ1_1.pack()
LJ1_2 = Label(Fscore_val1, textvariable=var_J1_2, font=font_score)
LJ1_2.pack()
LJ1_3 = Label(Fscore_val1, textvariable=var_J1_3, font=font_score)
LJ1_3.pack()
LJ1_4 = Label(Fscore_val1, textvariable=var_J1_4, font=font_score)
LJ1_4.pack()
LJ1_5 = Label(Fscore_val1, textvariable=var_J1_5, font=font_score)
LJ1_5.pack()
LJ1_6 = Label(Fscore_val1, textvariable=var_J1_6, font=font_score)
LJ1_6.pack()
LJ1_Bonus = Label(Fscore_val1, textvariable=var_J1_Bonus, font=font_score)
LJ1_Bonus.pack()
LJ1_TotSup = Label(Fscore_val1, textvariable=var_J1_TotalSup, font=font_score)
LJ1_TotSup.pack()
Label(Fscore_val1, text="", font=font_score).pack()
Label(Fscore_val1, text="", font=font_score).pack()
LJ1_Brelan = Label(Fscore_val1, textvariable=var_J1_Brelan, font=font_score)
LJ1_Brelan.pack()
LJ1_Carre = Label(Fscore_val1, textvariable=var_J1_Carre, font=font_score)
LJ1_Carre.pack()
LJ1_Full = Label(Fscore_val1, textvariable=var_J1_Full, font=font_score)
LJ1_Full.pack()
LJ1_Petite = Label(Fscore_val1, textvariable=var_J1_Petite, font=font_score)
LJ1_Petite.pack()
LJ1_Grande = Label(Fscore_val1, textvariable=var_J1_Grande, font=font_score)
LJ1_Grande.pack()
LJ1_Rien = Label(Fscore_val1, textvariable=var_J1_Rien, font=font_score)
LJ1_Rien.pack()
LJ1_Yams = Label(Fscore_val1, textvariable=var_J1_Yams, font=font_score)
LJ1_Yams.pack()
LJ1_Chance = Label(Fscore_val1, textvariable=var_J1_Chance, font=font_score)
LJ1_Chance.pack()
LJ1_TotInf = Label(Fscore_val1, textvariable=var_J1_TotalInf, font=font_score)
LJ1_TotInf.pack()
Label(Fscore_val1, text="", font=font_score).pack()
LJ1_Tot = Label(Fscore_val1, textvariable=var_J1_Total, font=font_score)
LJ1_Tot.pack()


###=======================================
Fscore_val2 = Frame(Fparam)
Fscore_val2.pack(side=LEFT, padx=(15,5))

LJ2 = Label(Fscore_val2, text="JOUEUR 2", font=fBo)
LJ2.pack()
#Variables de score du joueur 2
var_J2_1, var_J2_2, var_J2_3, var_J2_4 = StringVar(), StringVar(), StringVar(), StringVar()
var_J2_5, var_J2_6, var_J2_Bonus, var_J2_TotalSup = StringVar(), StringVar(), StringVar(), StringVar()
var_J2_Brelan, var_J2_Carre, var_J2_Full, var_J2_Petite = StringVar(), StringVar(), StringVar(), StringVar()
var_J2_Grande, var_J2_Rien, var_J2_Yams, var_J2_Chance, var_J2_TotalInf = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
var_J2_Total =StringVar()

LJ2_1 = Label(Fscore_val2, textvariable=var_J2_1, font=font_score)
LJ2_1.pack()
LJ2_2 = Label(Fscore_val2, textvariable=var_J2_2, font=font_score)
LJ2_2.pack()
LJ2_3 = Label(Fscore_val2, textvariable=var_J2_3, font=font_score)
LJ2_3.pack()
LJ2_4 = Label(Fscore_val2, textvariable=var_J2_4, font=font_score)
LJ2_4.pack()
LJ2_5 = Label(Fscore_val2, textvariable=var_J2_5, font=font_score)
LJ2_5.pack()
LJ2_6 = Label(Fscore_val2, textvariable=var_J2_6, font=font_score)
LJ2_6.pack()
LJ2_Bonus = Label(Fscore_val2, textvariable=var_J2_Bonus, font=font_score)
LJ2_Bonus.pack()
LJ2_TotSup = Label(Fscore_val2, textvariable=var_J2_TotalSup, font=font_score)
LJ2_TotSup.pack()
Label(Fscore_val2, text="", font=font_score).pack()
Label(Fscore_val2, text="", font=font_score).pack()
LJ2_Brelan = Label(Fscore_val2, textvariable=var_J2_Brelan, font=font_score)
LJ2_Brelan.pack()
LJ2_Carre = Label(Fscore_val2, textvariable=var_J2_Carre, font=font_score)
LJ2_Carre.pack()
LJ2_Full = Label(Fscore_val2, textvariable=var_J2_Full, font=font_score)
LJ2_Full.pack()
LJ2_Petite = Label(Fscore_val2, textvariable=var_J2_Petite, font=font_score)
LJ2_Petite.pack()
LJ2_Grande = Label(Fscore_val2, textvariable=var_J2_Grande, font=font_score)
LJ2_Grande.pack()
LJ2_Rien = Label(Fscore_val2, textvariable=var_J2_Rien, font=font_score)
LJ2_Rien.pack()
LJ2_Yams = Label(Fscore_val2, textvariable=var_J2_Yams, font=font_score)
LJ2_Yams.pack()
LJ2_Chance = Label(Fscore_val2, textvariable=var_J2_Chance, font=font_score)
LJ2_Chance.pack()
LJ2_TotInf = Label(Fscore_val2, textvariable=var_J2_TotalInf, font=font_score)
LJ2_TotInf.pack()
Label(Fscore_val2, text="", font=font_score).pack()
LJ2_Tot = Label(Fscore_val2, textvariable=var_J2_Total, font=font_score)
LJ2_Tot.pack()

can.create_text(wCan/2, hCan/2+50, text=var_mode.get(), font=("Tahoma", 15, "bold"), fill=current)
button_off()
###=======================================
#Boucle de la fenêtre
###=======================================
fen.mainloop()
