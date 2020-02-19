''' Gestion principale d'un jeu de Yams, module principal.

    @author: Rouyan Thi
'''


from random import sample, randint


def jet_init(nb_des, mode):
    '''Lance tous les dés une première fois.

    :param nb_des: nombre de dés à lancer
    :type nb_des: int
    :param mode: jeu avec ou sans dés cassés
    :type mode: int
    :return: renvoie la liste des valeurs des dés
    :rtype: list
    '''
    
    liste_des = []
    for n in range(nb_des):
        liste_des += [randint(1,6)]
    if mode == 1:
        k = randint(1, 100)
        pos_casse = [1, 1, 1, 1, 1]
        if k <= 5:
            a, b, c = randint(1, 5), randint(1, 5), randint(1, 5)
            des_casses = place_casses([a, b, c], pos_casse)
        elif k <=15:
            a, b = randint(1, 5), randint(1, 5)
            des_casses = place_casses([a, b], pos_casse)
        elif k <= 25:
            a = randint(1, 5)
            des_casses = place_casses([a], pos_casse)
        else:
            des_casses = [0, 0, 0, 0, 0]
        return [liste_des, des_casses]
    return liste_des
    

def relance(select, liste_des, mode):
    '''Relance les dés sélectionnés.

    :param select: sélection des dés à relancer
    :type select: list
    :param liste_des: valeurs des dés avant relance
    :type liste_des: list
    :return: renvoie les nouvelles valeurs des dés
    :rtype: list
    '''
    count = 0
    if mode == 0:
        for elem in select:
            if elem != 0 and elem[1] == liste_des[elem[0]]:
                liste_des[elem[0]] = randint(1, 6)
        return liste_des
    else:
        pos_casse = []
        for elem in select:
            if elem != 0 and elem[1] == liste_des[elem[0]]:
                liste_des[elem[0]] = randint(1, 6)
                pos_casse += [1]
                count += 1
            else:
                pos_casse += [0]
        k = randint(1, 100)
        if k <= 5 and count >= 3:
            a, b, c = randint(1, 5), randint(1, 5), randint(1, 5)
            des_casses = place_casses([a, b, c], pos_casse)
        elif k <= 15 and count >= 2:
            a, b = randint(1, 5), randint(1, 5)
            des_casses = place_casses([a, b], pos_casse)
        elif k <= 25 and count >= 1:
            a = randint(1, 5)
            des_casses = place_casses([a], pos_casse)
        else:
            des_casses = [0, 0, 0, 0, 0]
        return [liste_des, des_casses]


def place_casses(val_cassees, pos_casse):
    des_casses = [0, 0, 0, 0, 0]
    for elem in val_cassees:
        if elem == 1 and pos_casse[0] == 1:
            des_casses[0] = 1
        if elem == 2 and pos_casse[1] == 1:
            des_casses[1] = 1
        if elem == 3 and pos_casse[2] == 1:
            des_casses[2] = 1
        if elem == 4 and pos_casse[3] == 1:
            des_casses[3] = 1
        if elem == 5 and pos_casse[4] == 1:
            des_casses[4] = 1
    return des_casses

