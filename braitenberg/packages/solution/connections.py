from typing import Tuple

import numpy as np

#allgemeine Kommentare:
#äusserster Streifen rechts nicht beachten --> wenn Ente so weit am Rand ist kommt er sowieso daran vorbei
#ganzer oberer Bereich wird nicht beachtet: auf Duckies die so weit weg sind muss noch nicht reagiert werden

def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values

    res[250:, 100:200 ] = 0.8 
    # je näher DUckie kommt desto stärker reagiert Bot, weil er am Anfang nur schwach reagiert (gegenteilig zu rechter Matrix, damit sie sich gegenseitig nicht aufheben)
    
    res[220:300, 100:260] = 0.3 #Idee: Bot fängt früher an leicht nach rechts auszuweichen, wenn Duckie eher am LinkenRand bis weiter mittig auftaucht --> fährt weniger lange gerade darauf zu
    #Feld darf aber auch nicht zu gross sein, weil er sonst zu früh reagiert wenn einem Duckie auf rechter Seite ausgewichen werden muss 



    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    
    #Bot muss auch gegen links ausweichen/drehen können --> braucht "Reaktionsfeld" wo rechter Motor mehr dreht --> rotes Feld mitte/oben links auf rechter Matrix
    #klein und asymmetrische zu linker Matrix, damit sich Felder nicht "aufheben" resp. widersprechen
    res[200:300, 400:500] = 0.7
    res[200:300, 350:400] = 0.5 #Bot muss früher anfangen abzuderehen wenn Duckie mittig/rechts kommt
 
    res[300:400, 400:500] = 0.5 #Reaktion wird schwächer wenn Duckie näher kommt --> Idee: ist Duckie noch weiter weg wird stärker korrigert, wenn es näher kommt müssen wenn nötig
    #nur noch kleinere Anpassungen gemacht werden --> soll auch verhindern das Bot "überdreht" und z.B. dann direkt auf Duckie auf linker Seite zusteuert

    
    # ---
    return res
