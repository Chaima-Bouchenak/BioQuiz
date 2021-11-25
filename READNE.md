
///////////////////////////////////////////////////////////////////////////// README /////////////////////////////////////////////////////////////////////////////

### Bienvenue dans le readme de BioQuiz


//////////// installation ////////////

#### 1 - Pour consulter le site sur le seveur local :
 
    Appuiez sur code (bouton en haut a droite) et selectionner Download ZIP

    Une fois le repository télécharger décompresser le dossier BioQuiz-main.zip et l'extraire dans le dossier que vous souhaitez

Ouvrir un terminal

    Installer l'environnement conda pour django
    https://docs.conda.io/en/latest/miniconda.html

Create a conda environment avec la commande:

    conda create --name djangoenv python=3.8

    lancer la commande : conda activate djangoenv (Activer l'environnement conda )

    Se placer à la racine du projet (dans le dossier /BioQuiz-main)

    lancer la commande : pip install -r requirements.txt (pour installer toute les dependances)

    lancer la commande : python manage.py runserver (pour lancer le projet)

    ouvrez le lien affiché sur le terminal pour lancer le Quiz.

#### 2 - Pour le consulter sur un seveur distant : 

  Rendez-vous sur le lien suivant : https://bioquiz-app.herokuapp.com/
