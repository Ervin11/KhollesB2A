#!/usr/local/bin/python3.7

import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("-l", help="Affiche le contenu de la liste", action="store_true")
parser.add_argument("-a", type=int, help="Ajoute les elements dans liste.csv", nargs='+')
parser.add_argument("-c", help="Supprime tous les elements dans liste.csv", action="store_true")
parser.add_argument("-s", "--option", help="--max / --min / --moy", action="store_true")
parser.add_argument("--max", help="Affiche la valeur maximale dans liste.csv", action="store_true")
parser.add_argument("--min", help="Affiche la valeur minimale dans liste.csv", action="store_true")
parser.add_argument("--moy", help="Affiche la moyenne des valeurs de liste.csv", action="store_true")

args = parser.parse_args()

if args.l:
    
    with open('liste.csv', 'r') as liste:
        reader = csv.reader(liste)

        for row in reader:
            print(' '.join(row))

elif args.a:

    with open('liste.csv', 'a') as liste:
        writer = csv.writer(liste)
        writer.writerows([[a] for a in args.a])

elif args.c:

    truncate_list = open("liste.csv", "w+")
    truncate_list.close()

elif args.option:

    if args.max:

        with open('liste.csv', 'r') as liste:
            
            reader = csv.reader(liste)

            liste = []

            for row in reader:
                
                for x in row:
                
                    x = int(x)
                    liste.append(x)

            max_value = max(liste)
            print('Valeur maximale : ', max_value)

    elif args.min:

        with open('liste.csv', 'r') as liste:
            
            reader = csv.reader(liste)

            liste = []

            for row in reader:
                
                for x in row:
                
                    x = int(x)
                    liste.append(x)

            min_value = min(liste)
            print('Valeur minimale : ', min_value)
        
    elif args.moy:

        with open('liste.csv', 'r') as liste:
            
            reader = csv.reader(liste)

            liste = []

            for row in reader:
                
                for x in row:
                
                    x = int(x)
                    liste.append(x)

            avg = sum(liste)/len(liste)
            print('Moyenne : ', avg)
            print(sum(liste))
            print(len(liste))


        
        
        
        
            
    
    
