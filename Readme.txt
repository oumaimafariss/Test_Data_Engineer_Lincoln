## La structure du pipeline:

le pipeline est diviser en 4 etapes:
 -1er etape consiste à creer la table 'df_clin' permettant d'avoir le médicament, l'article scientifique, le journal et la date clinique 
 -2eme etape consiste à creer la table 'df_pub' permettant d'avoir le médicament, titre de l'article pubMed, le journal et la date pubMed
 -3eme etape consiste à creer la table 'df_journal' permettant d'avoir le médicament, le journal, la date clinique et la date pubMed
 -4eme etape consite à creer la table final 'df_final' permet d'avoir: le médicament, l'articl scientifique, titre de l'article pubMed, joural, date clinique et date de pubMed  

Vous trouverai sur le file Globl_test.ipynb tout le test et les resultats de chaque etape du test.
Les resultats des 4 etapes sités; ainsi que le scripte qui permet d'avoir le json file, ensuite la partie
Traitement ad-hoc et enfin la partie SQL.
-Les etapes 1,2,3 et 4 nous avons mis en .py files afin de les utiliser dans l'orchestrateur.
 En plus les étapes 1 et 2 peuvent etre utiliser pour avoir le résultzt de l'étape 3 et etape 4.

## le deploiement sera sur GCP:

la structure choisie aide a faire le doployement sur le cloud en utilisant Docker et Kubflow

la partie orchestrateur:

L’orchestrateur choisie pour créer notre data pipeline est Kubeflow pipeline car est une plateforme permettant de créer et de déployer des flux plus précisément les flux d'apprentissage automatique (ML) portables et évolutifs basés sur des conteneurs Docker. Après avoir déployer Kubeflow sur Google Cloud Platform et créer une image sur Docker Hub. Nous pouvons commencer le process du data pipeline. 
A l’aide de la fonction @kfp.dsl.component, nous allons créer les différents component du pipeline.
Dans la première component nous allons faire appel à la table clinique trials avec le langage python et le file ‘Etape1_Clinical_trials.py’ ensuite,  nous allons créer un autre component pour faire appel à la table pubmed, pareil pour la table journal et enfin la dernier composent pour avoir le fichier json qui représente un graphe de liaison entre les différents médicaments et leurs mentions respectives dans les différentes publications PubMed, les différentes publications scientifiques et enfin les journaux avec la date associée à chacune de ces mentions.
Pour l'encastrassions des 4 étapes nous allons utiliser la fonction @kfp.dsl.pipeline.
Cette fonction permet d’exécuter le pipeline étape par étape selon les components créer auparavant.

## Aller plus loin

Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses 
volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ?

- La taille du fichier : pour de gros fichiers, il faudra peut-être envisager de les diviser en plusieurs 
parties afin de faciliter leur traitement.

- Le nombre de fichiers : pour un grand nombre de fichiers, il faudra peut-être envisager de les traiter 
en parallèle et de louver des VM afin d'accélérer le processus.
