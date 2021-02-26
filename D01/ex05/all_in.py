import sys

states = {"Oregon": "OR", "Alabama": "AL", "New Jersey": "NJ", "Colorado": "CO"}
capital_cities = {"OR": "Salem", "AL": "Montgomery", "NJ": "Trenton", "CO": "Denver"}


def find_city(state):
    for code in states:
        if state.lower() == code.lower():
            city = states[code]
            return capital_cities[city]


def find_state(value):
    code = ''
    for land in capital_cities.items():
        if value.lower() == land[1].lower():
            code = land[0]
    for city in states.items():
        if code == city[1]:
            return city[0]


def my_split(str):
    values = str.split(',')
    #  print(values)
    for li in values:
        strip_val = li.strip()
        if strip_val:
            ret_state = find_state(strip_val)
            ret_city = find_city(strip_val)
            if ret_state is None and ret_city is not None:
                ret_state = find_state(ret_city)
            if ret_city is None and ret_state is not None:
                ret_city = find_city(ret_state)
            if ret_city is not None and ret_state is not None:
                print(ret_city, 'is the capital of', ret_state)
            if ret_city is None and ret_state is None:
                print(strip_val, 'is neither a capital city nor a state')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        my_split(sys.argv[1])
