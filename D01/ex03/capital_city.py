import sys


def find_city(argv):
    states = {"Oregon": "OR", "Alabama": "AL", "New Jersey": "NJ", "Colorado": "CO"}
    capital_cities = {"OR": "Salem", "AL": "Montgomery", "NJ": "Trenton", "CO": "Denver"}
    if len(sys.argv) != 2:
        return
    for code in states:
        if argv[0] == code:
            city = states[code]
            print(capital_cities[city])
            break
    else:
        print("Unknown state")


if __name__ == '__main__':
    find_city(sys.argv[1:])
