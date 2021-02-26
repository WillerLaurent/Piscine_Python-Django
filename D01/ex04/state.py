import sys


def find_state(argv):
    states = {"Oregon": "OR", "Alabama": "AL", "New Jersey": "NJ", "Colorado": "CO"}
    capital_cities = {"OR": "Salem", "AL": "Montgomery", "NJ": "Trenton", "CO": "Denver"}
    code = ''
    if len(sys.argv) != 2:
        return
    for land in capital_cities.items():
        if argv[0] == land[1]:
            code = land[0]
    for city in states.items():
        if code == city[1]:
            print(city[0])
            break
    else:
        print("Unknown capital city")


if __name__ == '__main__':
    find_state(sys.argv[1:])
