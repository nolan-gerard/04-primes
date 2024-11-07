"""
Dans cet exercice, on cherche à vérifier si plusieurs nombres sont premiers ou non.
On a donc écrit une fonction qui va vérifier si un nombre est premier ('isprime'),
et une autre fonction ('main') qui va appeller cette première fonction.
"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Cette fonction vérifie si un nombre est premier en le divisant par
    tous les nombres inférieurs à sa racine.
    Si le reste d'une division vaut 0 alors le nombre n'est pas premier.
    """
    if p==1:
        return False
    if p==2:
        return True
    premier=True
    for i in range(2, int(sqrt(p)+1)):
        if p%i==0:
            premier=False
            break
    return premier



#### Fonction principale


def main():
    """
    Cette fonction va appeller isprime plusieurs fois et donc
    vérifier si plusieurs nombres sont premiers.
    C'est aussi ici qu'on choisit ce qu'on veux afficher, 
    l'affichage ci dessous va écrire dans le terminal tous les nombres testés QUI SONT PREMIERS.
    """

    # vos appels à la fonction secondaire ici
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    # print()


if __name__ == "__main__":
    main()
