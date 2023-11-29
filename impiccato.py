# -*- coding: utf-8 -*-
"""
Gioco impiccato
"""
import random,sys
def omino(quanto_sbagliato : int) -> str:
    " rappresentazione omino impiccato "
    if quanto_sbagliato == 0:
        print("""
         ____
         |  |
         |
         |
         |
        _|__
        """
        )
    if quanto_sbagliato == 1:
        print("""
         ____
         |  |
         |  0
         |
         |
        _|__
        """
        )
    if quanto_sbagliato == 2:
        print("""
         ____
         |  |
         |  0
         |  |
         |
        _|__
        """
        )
    if quanto_sbagliato == 3:
        print("""
         ____
         |  |
         |  0
         |  |-
         |
        _|__
        """
        )
    if quanto_sbagliato == 4:
        print("""
         ____
         |  |
         |  0
         | -|-
         |
        _|__
        """
        )
    if quanto_sbagliato ==5:
        print("""
         ____
         |  |
         |  0
         | -|-
         | |
        _|__
        """
        )
    if quanto_sbagliato == 6:
        print("""
         ____
         |  |
         |  0
         | -|-
         | | |
        _|__
        """
        )
    
    
def parole_random(fileparole: str):
    with open(fileparole,mode="r",encoding="utf-8") as f:
        testo = f.read()
        parole = testo.split()
        parola_indovinare = random.choice(parole)
    return parola_indovinare

def trasforma_parola(parola: str) -> str:
    lunghezza_parola = len(parola)
    parola_nascota = lunghezza_parola * "*"
    return parola_nascota
    


def sostituzione_lettera(lettera_input: str,parola_normale: str, parola_nascosta: str) -> str:
    
    sbagliato = 0
    while sbagliato < 6:
        #scandisco tutta la parola
        for i in range(len(parola_normale)):
            if lettera_input == parola_normale[i]:
                parola_nascosta.replace(parola_normale[i], lettera_input)
            print(parola_nascosta)
            if lettera_input != parola_normale[i]:
                sbagliato += 1
            print(f"la lettera {lettera_input} non è presente nella parola")
            
        if parola_nascosta == parola_normale:
            print(f"bravo hai indovinato, la parola era {parola_normale} ")

        
    
    
    
#inizio gioco

scelta_lingua = input("En for english/ It per italiano: ")
scelta_lingua = scelta_lingua.lower()


#italiano
if scelta_lingua == "it":
    print("""========================
= Gioco dell'impiccato =
========================""")

    parola_generata = parole_random("parole.txt")
    parola_nascosta = trasforma_parola(parola_generata)

    #inizio gioco
    sbagliato = 0
    lista_lettere = list(parola_generata)
    lista_nascosta = list(parola_nascosta)




    while sbagliato < 6 :
    
        uomo = omino(sbagliato)
        parola_nascosta = "".join(lista_nascosta)
        print(f"parola da indovinare {parola_nascosta}")
        lettera_input = input("inserisci lettera o direttamente la parola: ")
    
        #caso eccezionale
        if lettera_input == parola_generata:
            print(f"indovinato, la parola era {parola_generata}")
            sys.exit()
        for lettera in parola_generata:
            if lettera_input == lettera:
                indice = lista_lettere.index(lettera_input)
                lista_lettere[indice] = 0
                lista_nascosta[indice] = lettera_input

        if lettera_input not in parola_generata:
            sbagliato += 1
        
        
        if "".join(lista_nascosta) == parola_generata:
            print(f"indovinato, la parola era {parola_generata}")
            sys.exit()

    uomo = omino(sbagliato)  
    print(f"hai perso! la parola era {parola_generata}")
    



#english version
if scelta_lingua == "en":
    print("""===========
= Hangman =
===========""")

    parola_generata = parole_random("words.txt")
    parola_nascosta = trasforma_parola(parola_generata)

    #inizio gioco
    sbagliato = 0
    lista_lettere = list(parola_generata)
    lista_nascosta = list(parola_nascosta)




    while sbagliato < 6 :
    
        uomo = omino(sbagliato)
        parola_nascosta = "".join(lista_nascosta)
        print(f"Guess the secret word {parola_nascosta}")
        lettera_input = input("insert the letter or the word: ")
    
        #caso eccezionale
        if lettera_input == parola_generata:
            print(f"you win!, the word was {parola_generata}")
            sys.exit()
        
        for lettera in parola_generata:
            if lettera_input == lettera:
                indice = lista_lettere.index(lettera_input)
                lista_lettere[indice] = 0
                lista_nascosta[indice] = lettera_input

        if lettera_input not in parola_generata:
            sbagliato += 1
        
        
        if "".join(lista_nascosta) == parola_generata:
            print(f"you win!, the word was {parola_generata}")
            sys.exit()

    uomo = omino(sbagliato)  
    print(f"You lose! the word was {parola_generata}")



