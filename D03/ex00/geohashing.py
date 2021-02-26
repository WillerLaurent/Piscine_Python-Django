import sys
import antigravity


def geohashing(coordonnees):
    if len(coordonnees) != 4:
        print("4 arguments sont nécessaires : <lat> <long> <date> <indice_dow>")
        print("Exemple : geohashing.py 37.421542 -122.085589 2005-05-26 10458.68")
        exit(1)
    try:
        lat = float(coordonnees[0])
        long = float(coordonnees[1])
        date = coordonnees[2]
        indice_dow = float(coordonnees[3])
        date_dow = date + '-' + str(indice_dow)
        antigravity.geohash(lat, long, date_dow.encode('ascii'))
    except ValueError:
        print("latitude,longitude et indice_dow doivent être de type float")
        print("Exemple : geohashing.py 37.421542 -122.085589 2005-05-26 10458.68")


if __name__ == '__main__':
    geohashing(sys.argv[1:])
