#!/usr/local/bin/python3.7

import argparse
import csv

# Parsing des options de commandes CLI

parser = argparse.ArgumentParser()
parser.add_argument("-l", help="Affiche le contenu de la liste", action="store_true")
parser.add_argument("-a", type=int, help="Ajoute les elements dans liste.csv", nargs='+')
parser.add_argument("-c", help="Supprime tous les elements dans liste.csv", action="store_true")
parser.add_argument("-s", help="--max / --min / --moy / --sum", action="store_true")
parser.add_argument("--max", help="Affiche la valeur maximale dans liste.csv", action="store_true")
parser.add_argument("--min", help="Affiche la valeur minimale dans liste.csv", action="store_true")
parser.add_argument("--moy", help="Affiche la moyenne des valeurs de liste.csv", action="store_true")
parser.add_argument("--sum", help="Affiche la somme des valeurs de liste.csv", action="store_true")
parser.add_argument("-t", help="Trie les elements de liste.csv dans l'ordre croissant / --desc", action="store_true")
parser.add_argument("--desc", help="Trie les elements de liste.csv dans l'ordre decroissant", action="store_true")


args = parser.parse_args()

# Si <nom_du_script> -l / Affiche tous les elements contenus dans liste.csv 
 
if args.l:
    
    with open('liste.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            print(' '.join(row))

# Si <nom_du_script> -a / Ajoute les arguments de type int dans liste.csv 

elif args.a:

    with open('liste.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows([[a] for a in args.a])

# Si <nom_du_script> -c / Supprime tous les elements contenus dans liste.csv 

elif args.c:

    truncate_list = open("liste.csv", "w+")
    truncate_list.close()

elif args.s:

    # Si <nom_du_script> -s --max / Affiche la valeur maximale contenu dans liste.csv

    if args.max:

        with open('liste.csv', 'r') as csvfile:
            
            reader = csv.reader(csvfile)

            liste = []

            for row in reader:
                
                for x in row:
                
                    x = int(x)
                    liste.append(x)

            max_value = max(liste)
            print('Valeur maximale : ', max_value)
    
    # Si <nom_du_script> -s --min / Affiche la valeur minimale contenu dans liste.csv

    elif args.min:

        with open('liste.csv', 'r') as csvfile:
            
            reader = csv.reader(csvfile)

            liste = []

            for row in reader:
                
                for x in row:
                
                    x = int(x)
                    liste.append(x)

            min_value = min(liste)
            print('Valeur minimale : ', min_value)

    # Si <nom_du_script> -s --moy / Affiche la moyenne de tous les elements contenus dans liste.csv
    
    elif args.moy:

        with open('liste.csv', 'r') as csvfile:
            
            reader = csv.reader(csvfile)

            liste = []

            for row in reader:
                
                for x in row:
                
                    x = int(x)
                    liste.append(x)

            avg = sum(liste)/len(liste)
            
            print('Moyenne : ', avg)
    
    # Si <nom_du_script> -s --sum / Affiche la somme de tous les elements contenus dans liste.csv

    elif args.sum:

        with open('liste.csv', 'r') as csvfile:
            
            reader = csv.reader(csvfile)

            liste = []

            for row in reader:
                
                for x in row:
                
                    x = int(x)
                    liste.append(x)

            summary = sum(liste)
            
            print('Somme : ', summary)
            
# Si <nom_du_script> -t / Affiche tous les elements contenus dans liste.csv dans l'ordre croissant

elif args.t:

        # Si <nom_du_script> -t --desc / Affiche tous les elements contenus dans liste.csv dans l'ordre décroissant

        if args.desc:

            with open('liste.csv', 'r') as csvfile:
                
                reader = csv.reader(csvfile)

                liste = []

                for row in reader:
                    
                    for x in row:
                    
                        x = int(x)
                        liste.append(x)
                
                liste.sort(reverse=True)
                print('Tri ordre décroissant : ', liste)
        
        else:

            with open('liste.csv', 'r') as csvfile:
                
                reader = csv.reader(csvfile)

                liste = []

                for row in reader:
                    
                    for x in row:
                    
                        x = int(x)
                        liste.append(x)
                
                liste.sort()
                print('Tri ordre croissant : ', liste)

        
        
        
        
            
    
    
