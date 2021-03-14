 
# <br>  APP FOR FOIL </br>

![foil](IMG/Readmefoil.jpg)

### [GitLab version](https://gitlab.com/simplon-dev-data-nantes-2020/brief-backup-bdd/-/tree/Matthias_Mews-Joris_Tessier/) | [GitHub version](https://github.com/Xiiuki/Foil)

## <br> Collab : </br>

   - Joris Tessier | [Github](https://github.com/joris-devdata), [LinkedIn](https://www.linkedin.com/in/joris-teyssier-1235351b6/)
    
   - Matthias Mews | [GitHub](https://github.com/Xiiuki), [LinkedIn](https://www.linkedin.com/in/matthias-mews/)

## <br>  Contexte du projet : </br>

Après avoir vu les images de l’America’s cup dans la baie d’Auckland, Cléante de Nantes a décidé de se mettre au catamaran avec foil.

Avant d’investir dans son engin high tech, elle a décidé de faire une petite application pour sa montre connectée qui donne en temps réel les dernières mesures sur 3 stations locales disposant d’un anémomètre. Elle souhaite savoir où se diriger pour trouver le vent nécessaire à ses futures activités.

Malheureusement sa montre dispose d’un stockage particulièrement réduit, donc la base de données locale devra être mise à jour régulièrement tout en s’assurant de ne pas dépasser un volume de stockage correspondant aux 10 derniers enregistrements. Enfin, un tantinet paranoïaque, elle souhaite absolument avoir la dernière sauvegarde qui devra être mise à jour régulièrement (une fois tous les 5 enregistrements).


## <br> Livrables : </br> 
--------

    ├── README.md              <--- Descriptif du projet
    │
    │
    ├── Backup                 <--- Dossier de sauvegarde de la base de données
    │
    │
    ├── IMG                    <--- Dossier d'images 
    │
    │
    ├── Database.ipynb         <--- Permet de créer la database winds sous sqlit3
    │
    │
    ├── Application.ipynb      <--- Permet de lancer l'application 
    │
    │
    ├── utils.py               <--- Regroupement de tout les scripts pour le bon fonctionnement de l'application 
    │
    │
    └── requirements.txt       <--- Fichier .txt qui regroupe toutes les librairis utiliser pour le bon fonctionnement du projet

--------

## <br> Requirements : </br>

   - python 3.8.6 + requirements.txt
    
   - DB Browser ([dowload](https://sqlitebrowser.org/dl/))

## <br> Installation </br>


Le clone du projet et sa bonne installation sur votre pc :

- Le clonage :
 
 
  - With github :
  
    ```
    cd c:/
    mkdir Appfoil
    cd Appfoil/
    git clone git@github.com:Xiiuki/Foil.git
    cd Foil/                                                                    
    ```
    
  - With Gitlab :
    
    ```
    cd c:/
    mkdir Appfoil
    cd Appfoil/
    git clone git@gitlab.com:simplon-dev-data-nantes-2020/brief-backup-bdd.git  
    cd brief-backup-bdd/                                                                    
    ```
  
 
 - Création de l'environnement virtuelle :
 
    ```
    python -m venv *nom_env*
    source *nom_venv*/Scripts/activate
    ```
     
     
 - Installation des librairies :
    
    ```
    python -m pip install pip --upgrade
    pip install -r requirements.txt
    pip freeze
    ```
    
 - Lancer le notebook :
    
    ```
    jupyter-lab
    ```
    
    
## <br> Exécution de l'application </br>

Dans un premier temps, veuillez créer la database `winds`, pour cela lancez [Database](01_Database.ipynb) le scripts comprends aussi une création de table.

Puis il vous suffit simplement de lancer l'[application](02_Application.ipynb).



## <br> Attention : </br>

Si vous utilisez Gitlab, pensez bien à changer les path dans la fonction `def create_copy_db():` qui se trouve dans [utils](utils.py)


## <br> Petit plus : </br> 

Si vous le désirez, vous pouvez visualiser la database sur DB Beaver.

Pour cela, après l'exécution de l'application, ouvrez DB Beaver, ouvrez la base de données `winds` et actualiser celle-ci de temps en temps pour voir son évolution.

## <br> Ressources : </br>



Site openwinmap qui regroupe les stations pioupiou :

https://www.openwindmap.org/PP113


API utilisée par openwinmap, et utilisée pour le projet :


http://developers.pioupiou.fr/api/live/
