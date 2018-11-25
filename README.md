
# Programme CLI en Python qui permet : 

- d'écrire des nombres dans un fichier CSV
- d'en afficher le contenu
- d'en supprimer le contenu
- d'afficher la valeur maximale
- d'afficher la valeur minimale
- d'afficher la moyenne des valeurs
- d'afficher la somme des valeurs
- de trier et afficher les valeurs dans un ordre croissant
- de trier et afficher les valeurs dans un ordre décroissant

# Options de commande :

  - -h, --help    / Affiche cette aide
  - -l            / Affiche le contenu de la liste
  - -a [int]      / Ajoute 1 ou plusieurs elements dans liste.csv
  - -c            / Supprime tous les elements dans liste.csv
  - -s            / --max / --min / --moy / --sum
  - --max         / Affiche la valeur maximale dans liste.csv
  - --min         / Affiche la valeur minimale dans liste.csv
  - --moy         / Affiche la moyenne des valeurs de liste.csv
  - --sum         / Affiche la somme des valeurs de liste.csv
  - -t            / Trie les elements de liste.csv dans l'ordre croissant / --desc
  - --desc        / Trie les elements de liste.csv dans l'ordre decroissant

# Exemple d'utilisation

Insertion d'elements : 

- ./SALIF_Ervin_kholle_1.py -a 1 2 10 43 21 102 5 

Affichage du contenu du fichier CSV :

- ./SALIF_Ervin_kholle_1.py -l

Affichage de la valeur maximale : 

- ./SALIF_Ervin_kholle_1.py -s --max

Affichage de la valeur minimale : 

- ./SALIF_Ervin_kholle_1.py -s --min

Affichage de la moyenne :

- ./SALIF_Ervin_kholle_1.py -s --moy

Affichage de la somme :

- ./SALIF_Ervin_kholle_1.py -s --sum

Affichage dans l'ordre croissant :

./SALIF_Ervin_kholle_1.py -t

Affichage dans l'ordre decroissant :

./SALIF_Ervin_kholle_1.py -t --desc
