import re
import random
import os


def pendus():
    pseudo = input('Entre ton pseudo : ')
    listmot = ['ordinateur']
    nbaléatoire = random.randint(0, len(listmot)-1)
    motpendu = listmot[nbaléatoire]
    motcaché = str()
    for i in motpendu:
        motcaché = motcaché + 'x'
    print('Mot a déviner : ', motcaché)
    nbdevie = 8
    while nbdevie > 0:
        lettre = input(f'Entré une lettre ')
        x = 0 # nb de lettre trouvé
        for i in range(0,len(motcaché)):
            if lettre == motpendu[i]:
                lmotcaché = list(motcaché)
                lmotcaché[i] = motpendu[i]
                motcaché = ''.join(lmotcaché)
                x += 1
        if x != 0:
            print(f'bravo tu a trouvé {x}\n Le mot est {motcaché}')
            if motcaché == motpendu: #si win
                print(f'Bravo tu a gagnés tu marques donc {nbdevie} point(s)')
                ajoutpoint(pseudo, nbdevie)
                exit()
        else:
            nbdevie -= 1
            print(f"Tu n'as pas trouvé de lettre il te reste {nbdevie} chance(s)")

    print('Tu a perdu dommage')
    exit()

def ajoutpoint(pseudo,point):
    #besoin d import os
    currentpath = os.path.dirname(os.path.abspath(__file__)) + "/"
    f = open(currentpath + 'datapendu.txt', "r") # f = fichier pendu
    data = f.read()
    f.close
    lpseudo = re.findall('--(.*)--', data)
    lpoint = re.findall('::(.*)::', data)
    b = 0
    print('lpoint', lpoint)
    for i in range(0, len(lpseudo)):
        if pseudo == lpseudo[i]: #si le joueur existe deja
            lpoint[i] = int(lpoint[i]) + point
            b = 1
    if b ==0:              #s'il existe pas
        lpseudo.append(pseudo)
        lpoint.append(point)
    lpp = list()  #liste pseudo points
    a = 0
    for i in range(0, len(pseudo)-1):  #crée la liste
        a = 1
        try:
            lpp.append(f'--{lpseudo[i]}--')
            lpp.append(f'::{lpoint[i]}::')
        except:
            pass

    if a == 0: #premiere fois
        lpseudo.append(pseudo)
        lpoint.append(point)
        lpp.append(f'--{lpseudo[0]}--')
        lpp.append(f'::{lpoint[0]}::')

    newdata = '\n'.join(lpp)
    f = open(currentpath + 'datapendu.txt', "w")  # f = fichier pendu
    f.write(newdata)

def main():
    pendus()

if __name__ == "__main__":
    main()

#motcaché = re.sub('(.)[a-z]', 'x', motpendu)