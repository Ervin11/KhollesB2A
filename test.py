#!/usr/local/bin/python3.7

import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("-l", help="Affiche le contenu de la liste", action="store_true")
parser.add_argument("-a", type=int, help="Ajoute les elements dans liste.csv", nargs='+')
parser.add_argument("-c", help="Supprime tous les elements de la liste", action="store_true")
parser.add_argument("-s", "--max", help="Affiche la valeur maximum de la liste", action="store_true")

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

elif args.max:

    with open('liste.csv', 'r') as liste:
        reader = csv.reader(liste, dialect='excel')

        tab = []

        for row in reader:
            for x in row:
                x = int(x)
                tab.append(x)

        yo = max(tab)
        print(yo)



        
        
        
        
            
    
    
