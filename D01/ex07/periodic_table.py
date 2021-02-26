def read_file():
    file = open("periodic_table.txt", "r")
    text = file.read().split('\n')
    tab = {}
    for i in range((len(text) - 1)):
        tmp = text[i].split(',')
        name = tmp[0].split('=')
        position = name[1].split(':')
        number = tmp[1].split(':')
        small = tmp[2].split(':')
        molar = tmp[3].split(':')
        tab["name"] = name[0]
        tab["position"] = position[1]
        tab["number"] = number[1]
        tab["small"] = small[1]
        tab['molar'] = molar[1]
    file.close()
    return tab


def create_html(f):
    f.write("<!DOCTYPE html><html lang='en'><head><title>periodic_table</title><meta charset='utf-8'></head><body>")
    f.write("<h2>Mendeleev's table</h2><table style='border:solid 1px pink;'>")

    f.write("</html>\n")


def write_to_file(tab):
    with open("periodic_table.html", "w") as f:
        create_html(f)


if __name__ == '__main__':
    table = read_file()
    write_to_file(table)
