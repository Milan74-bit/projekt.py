'''
Projekt_1 engeto
author = Milan Povolný
ja.mida@seznam.cz
'''

# registrovaní uživatelé
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# texty k procházení

texty = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
# uvítání a žádost k přihlášení:
print("Vítej v aplikaci na analýzu textu, po přihlášení můžeš začít.")
username = input("Zadejte uživatelské jmeno:\n")
password = input("Zadejte heslo:\n")

# podmínka pro přihlášení

if username in users and users[username] == password:
    print(f"Vítej v aplikaci, {username}: Můžeš začít analyzovat texty:")
    vyber_textu = (input("Vyberte text 1 ,2 nebo 3:\n"))
    
    # proměné mám česky, anglicky se mi to pletlo:
    
    if vyber_textu.isdigit() and 1 <= int(vyber_textu) <=3:
        vybrany_text = texty[int(vyber_textu)-1]
        slova = vybrany_text.split()
        pocet_slov = len(slova)
        pocet_slov_velké_pismeno = sum(1 for slovo in slova if slovo.istitle())
        pocet_slov_velka_pismena = sum(1 for slovo in slova if slovo.isupper())
        pocet_slov_mala_pismena = sum(1 for slovo in slova if slovo.islower())
        pocet_cisel = sum(1 for slovo in slova if slovo.isdigit())
        součet_cisel = sum(int(slovo) for slovo in slova if slovo.isdigit())
# výpis hodnot:
        print(f"Pocet slov: {pocet_slov}")
        print(f"Počet slov začínajících velkým písmenem: {pocet_slov_velké_pismeno}")
        print(f"Počet slov psaných velkými písmeny: {pocet_slov_velka_pismena}")
        print(f"Počet slov psaných malými písmeny: {pocet_slov_mala_pismena}")
        print(f"Počet čísel: {pocet_cisel}")
        print(f"Součet všech čísel: {součet_cisel}")
# tabulka/graf počet písmen ve slovech od jedné:
        delka_slov = {}
        for slovo in slova:
            delka = len(slovo)
            if delka in delka_slov:
                delka_slov[delka] += 1
            else:
                delka_slov[delka] = 1
  #Výpis hodnot:      
        print("Tabulka slov dle počtu písmen:")
        print("-----------------------------")            
        print(" DÉLKA|  POČET VÝSKYTŮ  | NR:")
        print("-----------------------------")
        for delka, pocet in sorted(delka_slov.items()):
            print(f"{delka:>5} |{"*" * pocet:<16} | {pocet}")
    
    else: 
        print("Neplatný výběr ukončiji program!") 
else:
    print(f"Uživalel, {username}: s heslem {password} , není registrován, ukončuji program!")