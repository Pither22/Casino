from random import randrange
import os
import time

nombre = 0
mise = 0
argent = 100
continuer = True

print("Bienvenue au jeu de la roulette ! ")

def choisir_un_nombre():

    global nombre

    nombre = input("\nVeuillez choisir un nombre entre 0 et 49: ")
    nombre = int(nombre)

    if nombre < 0 or nombre > 49:
        choisir_un_nombre()
    else:
        print ("Vous avez choisis le nombre :", nombre)
        
    return nombre

def miser():

    global mise
    
    mise = input("\nVeuillez choisir une mise: ")
    mise = float(mise)

    if mise < 0:
        print("\nVous devez miser une somme positive")
        miser()
    elif mise > argent:
        print("\nVous n'avez pas assez d'argent pour miser une telle somme.\nVotre aegent: ", argent, "$")
        miser()
    
while continuer == True:

    choisir_un_nombre()
    print("\nVous disposez de ", argent, "$")
    miser()
    resultat_roulette = randrange(50)
    print("\nLa roulette est tombée sur le nombre.....", resultat_roulette)

    if resultat_roulette == nombre:

        gain = mise * 3

        print("\nET C'EST GAGNÉ !!!")
        print("Vous remportez 3 fois votre mise, soit la somme de ", gain, "$ !!")

        argent = argent + gain
    
        print("Votre cagnotte est maintenant de ", argent, "$")
    
    elif resultat_roulette % 2 == nombre % 2:

        gain = mise / 2
    
        print("\nC'est gagné ! Vous avez trouvé la bonne couleur, vous remportez 50% de votre mise ! Soit ", gain, "$")
    
        argent = argent + gain
    
        print("Votre cagnotte est maintenant de ", argent, "$")
    
    else:

        print("\nDésolé... C'est la banque qui gagne !")
        print("Vous perdez ", mise, "$")
    
        argent = argent - mise
    
        print("Votre cagnotte est maintenant de ", argent, "$")
    
    if argent <= 0:
    
        print("Vous n'avez plus d'argent ! Sortez d'ici !")
        time.sleep(3)
        continuer = False
        
    else:
        
        def oui_non():
        
            jouer = input("\nDésirez-vous continuer à jouer ? o/n")

            global continuer 
        
            if jouer.lower() == "n":
        
                continuer = False
                print("Au revoir !")
            
            elif jouer.lower() == "o":
        
                continuer = True 
            
            else:
        
                print("Veuillez choisir 'o' ou 'n' ")
                oui_non()

        oui_non()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
