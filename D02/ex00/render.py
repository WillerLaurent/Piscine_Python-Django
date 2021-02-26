import sys
import os
import re


def render(filename):
    if len(sys.argv) != 2:
        print("usage : render.py <file>.template")
        sys.exit(0)
    tmp = filename[0].split(".")
    file_ext = tmp[1]
    if file_ext != "template":
        print("The extend file must be '.template'")
    param = {}  # creation dictionnaire
    try:
        with open("settings.py", 'r') as f_set:
            for line in f_set:
                tmp = line.split('=')
                param[tmp[0].strip(' ')] = tmp[1].strip('\n \"') #j'assigne les clés/valeurs et je nettoie les données
    except FileNotFoundError as e:
        print("Le fichier {} n'existe pas.".format(e.filename))
        exit(1)
    except PermissionError as e:
        print("Droits de lecture absents sur le fichier {}".format(e.filename))
        exit(2)

    fd = open("CV.html", 'w')
    with open(filename[0], 'r') as infile:
        try:
            for line in infile:
                for cle in param:
                    line = line.replace("{"+cle+"}", param[cle])
                fd.write(line)
        except FileNotFoundError as e:
            print("Le fichier {} n'existe pas.".format(e.filename))
            exit(1)
        except PermissionError as e:
            print("Droits de lecture absents sur le fichier {}".format(e.filename))
            exit(2)


if __name__ == '__main__':
    render(sys.argv[1:])
