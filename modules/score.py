'''Module de score.

    @author: Rouyan Thi
'''

##===============================================
#Score de la partie supérieure
##===============================================
def un(liste_des):
    score = 0
    for elem in liste_des:
        if elem == 1:
            score += 1
    return score

    
def deux(liste_des):
    score = 0
    for elem in liste_des:
        if elem == 2:
            score += 2
    return score


def trois(liste_des):
    score = 0
    for elem in liste_des:
        if elem == 3:
            score += 3
    return score


def quatre(liste_des):
    score = 0
    for elem in liste_des:
        if elem == 4:
            score += 4
    return score


def cinq(liste_des):
    score = 0
    for elem in liste_des:
        if elem == 5:
            score += 5
    return score


def six(liste_des):
    score = 0
    for elem in liste_des:
        if elem == 6:
            score+= 6
    return score


def bonus(score_sup):
    '''Vérifie si le bonus est appliquable.

    :param score_sup: valeur du score de la partie supérieure
    :type score_sup: int
    :return: renvoie le score_sup avec ou sans bonus
    :rtype: int
    '''
    
    return score_sup >= (1+2+3+4+5+6)*3



##===============================================
#Score de la partie inférieure
##===============================================
def compare(liste_des):
    '''Compte le nombre de fois que chaque valeur est apparu dans le jet de dés.

    :param liste_des: valeur des cinq dés
    :type liste_des: list
    :return: renvoie le nombre de chaque dés
    :rtype: liste
    '''
    
    val = [0, 0, 0, 0, 0, 0]
    for elem in liste_des:
        if elem == 1:
            val[0] += 1
        elif elem == 2:
            val[1] += 1
        elif elem == 3:
            val[2] += 1
        elif elem == 4:
            val[3] += 1
        elif elem == 5:
            val[4] += 1
        elif elem == 6:
            val[5] += 1
    return val

    
def brelan(liste_des):
    controle = compare(liste_des)
    val_max = 0
    for n in range(len(controle)):
        if controle[n] >= 3:
            val_max = n+1
            break
    if val_max != 0:
        score = 0
        for n in range(len(controle)):
            score += controle[n] * (n+1)
        return score
    else:
        return False


def carre(liste_des):
    controle = compare(liste_des)
    val_max = 0
    for n in range(len(controle)):
        if controle[n] >= 4:
            val_max = n+1
            break
    if val_max != 0:
        score = 0
        for n in range(len(controle)):
            score += controle[n] * (n+1)
        return score
    else:
        return False


def full(liste_des):
    controle = compare(liste_des)
    yams, val_max, val_min = 0, 0, 0
    for n in range(len(controle)):
        if controle[n] == 5:
            yams = n+1
        if controle[n] == 3:
            val_max = n+1
        if controle[n] == 2:
            val_min = n+1
    if (val_max != 0 and val_min != 0) or yams != 0:
        return 25
    else:
        return False


def petite(liste_des):
    controle = compare(liste_des)
    suite = 0
    for n in range(len(controle)):
        if controle[n] >= 1:
            suite += 1
        else:
            suite = 0
        if suite == 4:
            break
    if suite == 4:
        return 30
    else:
        return False


def grande(liste_des):
    controle = compare(liste_des)
    suite = 0
    for n in range(len(controle)):
        if controle[n] == 1:
            suite += 1
        else:
            suite = 0
        if suite == 5:
            break
    if suite == 5:
        return 40
    else:
        return False


def yams(liste_des):
    controle = compare(liste_des)
    for n in range(len(controle)):
        if controle[n] == 5:
            return 50
    return False


def chance(liste_des):
    score = 0
    for elem in liste_des:
        score += elem
    return score
