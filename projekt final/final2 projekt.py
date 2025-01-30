"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Milan Povolný
email: ja.mida@seznam.cz
"""


import random
import time

def pozdrav_uživatele():
    print("Vítejte ve hře Bulls and Cows!:")
    print("Vygeneroval jsem tajné 4 místné číslo které nezačíná nulou a obsahuje unikátní číslice:")
    print("Vaším úkolem je uhodnout číslo, přeji hodně štěstí:")

def generuj_tajné_cislo():
    """ generuje čtyřciferné unikátní náhodné číslo nezačínající nulou
    """
    cisla = list("123456789")
    random.shuffle(cisla)
    tajne_cislo = cisla[:4]
    return "".join(tajne_cislo)

def zadej_platný_vstup(vstup):
    """ vyžádá od uživatele čtyřciferné číslo
    nesmí začínat nulou, 
    """
    if len(vstup) !=4:
        print("číslo musí mít 4 číslice") 
        return False
    if not vstup.isdigit():
        print("číslo musí být číslice")
        return False 
    if vstup[0] == "0":
        print("číslo nesmí začínat nulou")
        return False 
    if len (set(vstup)) !=4:
        print("číslo musí obsahovat unikátní číslo") 
        return False
    return True  

def vyhodnot_tip(tip, tajne_cislo):
    bulls = sum(1 for t,s in zip(tip, tajne_cislo)if t == s)
    cows = sum(1 for t, in tip if t in tajne_cislo)-bulls  
    return bulls, cows

def hraj_hru():
    pozdrav_uživatele()
    tajne_cislo = generuj_tajné_cislo()
    cas_hry = time.time()
    pokusy = 0

    while True:
        tip = input("Zadej svůj tip na číslo:\n")
        if not zadej_platný_vstup(tip):
           continue
        pokusy +=1
        bulls, cows = vyhodnot_tip(tip, tajne_cislo)
        if bulls == 1:
            print(f"{bulls} bull")
            
        else:
            print(f"{bulls} bulls")
            
        if cows == 1:
            print(f"{cows}cow")
             
        else:
            print(f"{cows} cows")
            
        if bulls == 4:
            konec_casu = time.time() 
            print(f"Výborně! Uhodli jste číslo na {pokusy} pokusů.") 
            print(f"Hádání trvalo { konec_casu - cas_hry:2f} sekund. ")         
            break

if __name__=="__main__":
    hraj_hru()
