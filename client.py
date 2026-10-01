import requests

# Formats.
ESC: str = "\033"
WARN: str = "/!\\"
BOLD: int = 1
WHITE: int = 37
BLUE: int = 34
RED: int = 31
GREEN: int = 32

def f(style: int, color: int) -> str:
    """ Formatte la chaine de style ANSI."""
    return f"{ESC}[{style};{color}m"

def encode(chaine):
    """ Chiffre l'adresse en chiffres. """
    nb = ""
    for c in chaine:
        val = str(ord(c))
        nb += (3 - len(val)) * "0" + val
    return nb

def main() -> None:
    """
    Liste des commandes
    - help 
    - connect
    - disconnect
    - goto
    - quit
    """
    print(f"{f(BOLD, WHITE)}Welcome to U_Search !\n")
    print(f"Tapez {f(BOLD, BLUE)}help{f(BOLD, WHITE)} pour consulter la documentation")
    cmd = ""
    name_serv = None
    
    while cmd != "quit":
        cmd = input(f"{f(BOLD, WHITE)}>> {f(BOLD, BLUE)}")
        print(f(BOLD, WHITE), end="")

        if cmd == "connect":
            if name_serv == None:
                name_serv = input(f"{f(BOLD, WHITE)}Entrez l'URL de votre serveur : ")
                print(f"{f(BOLD, WHITE)}Vérification...")
                reponse = requests.get(name_serv)
                if reponse.status_code == 200 :
                    if reponse.text == "[\"Welcome to U_Web !\"]":
                        print(f"{f(BOLD, GREEN)}URL correcte ! Bon voyage !{f(BOLD, WHITE)}")
                    else :
                        print(
                            f"{f(BOLD, RED)}Something went wrong... Veuillez recommencer\n{WARN} "
                            f"Il est nécessaire d'inclure https:// ou http://{f(BOLD, WHITE)}"
                        )
                        name_serv = None
            else :
                print(f"{f(BOLD, WHITE)}Vous êtes déjà connecté. Tapez disconnect pour vous déconnecter")

        elif cmd == "disconnect":
            name_serv = None
            print(f"{f(BOLD, GREEN)}Vous avez été déconnecté avec succés{f(BOLD, WHITE)}")

        elif cmd == "goto":
            if name_serv == None:
                print(f"{f(BOLD, RED)}Vous n'êtes pas connecté. Tapez {f(BOLD, BLUE)}connect{f(BOLD, WHITE)} pour vous connecter")
            else :
                address = input(f"{f(BOLD, WHITE)}Où souhaitez vous aller ? ")
                print(f"{f(BOLD, WHITE)}Encodage...")
                address = encode(address)
                print(f"{f(BOLD, GREEN)}URL encodé avec succés")
                print(f"{f(BOLD, WHITE)}Continuez votre voyage ici : {name_serv}/get/{address}")

        elif cmd == "quit":
            print(f"{f(BOLD, WHITE)}Merci d'avoir utilisé U_Web ! Bonne journée !")

        elif cmd == "help":
            print(f"{f(BOLD, WHITE)}Listes des commandes d'U_Search : ")
            print(f"{f(BOLD, BLUE)}connect : {f(BOLD, WHITE)}permet de renseigner le serveur à utiliser ({WARN} Il est nécessaire d'inclure https:// ou http:// dans l'URL)")
            print(f"{f(BOLD, BLUE)}disconnect : {f(BOLD, WHITE)}premet de de retirer le serveur actuel")
            print(f"{f(BOLD, BLUE)}goto : {f(BOLD, WHITE)}permet d'obtenir l'URL d'un lien ({WARN} Il est nécessaire d'inclure https:// ou http:// dans l'URL)")
            print(f"{f(BOLD, BLUE)}quit : {f(BOLD, WHITE)}quitte U_Search")
            print()

        else :
            print(f"{f(BOLD, RED)}Commande non reconnue ! Tapez help pour consulter la liste des commandes{f(BOLD, WHITE)}")
            
main()
