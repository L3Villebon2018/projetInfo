import serial
k='uid'
u='bebe'
print('%s%s'%(k,u))


let = '11010111'
def pick_lettre():
    codeMorse=[
        10111,
        111010101,
        11101011101,
        1110101,
        1,
        101011101,
        111011101,
        1010101,
        101,
        1011101110111,
        111010111,
        101110101,
        1110111,
        11101,
        11101110111,
        10111011101,
        1110111010111,
        1011101,
        10101,
        111,
        1010111,
        101010111,
        101110111,
        11101010111,
        1110101110111,
        11101110101
    ]
    return




def trie_phrase(vrai_phrase):
    l_liste = len(vrai_phrase)
    phrase_utile = []
    for i in range (1,l_liste - 8):#9 parce que l'on veut enlever les 8 derniers chiffres et le premier (0)
        phrase_utile.append(vrai_phrase[i])
    return phrase_utile


def decodage_lettre(phrase_utile,tableau_de_lettre):
    stop = 0
    while len(phrase_utile) != 0:
        #k='uid'
        #u='bebe'
        #print('%s%s'%(k,u))
        longueur = len(phrase_utile) - 1
        lettre = ''
        for i in range (longueur):
            if phrase_utile[i] == 0 and phrase_utile[i+1] == phrase_utile[i]:
                while stop == 0:
                    emplace_dans_lettre = i + 2
                    if phrase_utile[emplace_dans_lettre] == 0 and phrase_utile[emplace_dans_lettre] == phrase_utile[emplace_dans_lettre + 1]:
                        stop = 1
                    else:
                        lettre = '%s%s'%(lettre,str(phrase_utile[emplace_dans_lettre]))
                    i += 1

        longueur_lettre = len(lettre) + 2
        print(longueur_lettre)
        if len(phrase_utile) == longueur_lettre + 2:
            for j in range(longueur_lettre + 2):
                del phrase_utile[0]
            tableau_de_lettre.append(lettre)
            return tableau_de_lettre
        else:
            for j in range(longueur_lettre):
                del phrase_utile[0]
            tableau_de_lettre.append(lettre)
            tableau_de_lettre = decodage_lettre(phrase_utile,tableau_de_lettre)
            return tableau_de_lettre







vrai_phrase=[]
liste_bit =[]
debut = 0
fin = False
stop = False
stop_inside_2 = False
test = [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,0,1,1,1,0,0,1,0,1,0,1,1,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0]
j=0
while not stop:
    #csl = serial.Serial("COM8", 9600, timeout=5)
    #bit = csl.readline().decode().strip()
    #liste_bit.append(bit)
    liste_bit.append(test[j])
    if len(liste_bit) >= 13 and debut != 1:
        stop_inside_1 = False
        for i in range(13):
            if stop_inside_1 == 0:
                if liste_bit[-i-1] == 1:
                    if i == 12:
                        debut = 1
                        print("coucou")
                else:
                    stop_inside_1 = 1

    if debut :
        print(vrai_phrase)
        vrai_phrase.append(test[j])
        if len(vrai_phrase) >= 8:
            stop_inside_2 = False
            for i in range(8):
                if stop_inside_2 == 0:
                    print(vrai_phrase)
                    if vrai_phrase[-i-1] == 1:
                        if i == 7:
                            stop = 1
                    else:
                        print("hey")
                        stop_inside_2 = 1
    j += 1

phrase_utile = trie_phrase(vrai_phrase)
print(phrase_utile)
tableau_de_lettres = decodage_lettre(phrase_utile,[])
print(tableau_de_lettres)




