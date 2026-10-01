# U_Search
A travers la librairie FastAPI, permet d'accéder à des pages Web
### Dépendances
- requests 
- fastapi

Respectivement :
> pip install requests
> 
> pip install fastapi
## API
### Fonctionnement
1) Le lien demandé par l'utilisateur est chiffré (cf : encode) pour éviter de potentiels sécurités et une lecture par l'administrateur réseau 
2) Le lien est déchiffré sur le serveur
3) La page demandé est requests (avec la librairie du même nom)
4) Cette page est renvoyé à l'utilisateur
### Déploiement (sur un serveur FastAPI Cloud)
1) S'assurer de posséder un compte FastAPI Cloud
2) Créer un environnement virtuel avec main.py et requirements.txt
3) Installer FastAPI[standard] si non présent sur le PC
4) Entrer "fastapi deploy" dans une console 
5) Suivre les instructions de la console 
## Client
### Dépendance
- Uniquement requests
### Utilisation
- Tapez help pour obtenir le guide du client
## Notes
L'API est utilisable par n'importe qui possédant le lien, il est nécessaire de le garder confidentiel

FastAPI Cloud est en capacité de voir les requêtes faites et donc, les pages demandées

Les liens doivent passés par le client pour pouvoir être utilisable

Il n'y a pas de modifications de la page initiale (ou très peu), il est donc normal que certaines ressources (Images, CSS, JS) ne s'affichent pas

## Crédits
Un grand merci à Detroix23 pour les réformatages, l'aide apporté et la documentation !

### Contact
Pour obtenir de l'aide ou des clarifications, je suis contactable sur Discord sous le pseudonyme @f.ynn
