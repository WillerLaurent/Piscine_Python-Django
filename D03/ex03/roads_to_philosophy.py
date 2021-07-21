import requests, sys
from bs4 import BeautifulSoup


roads = ['Number']


def find_title(soup):
    title = soup.title
    title = str(title)
    end = title.find(" - Wikipedia")
    start = 7
    title = title[start:end]
    return title


def find_title_a_tag(text):
    start = text.find('>')
    end = text.find("</a>")
    title_a_tag = text[start + 1: end]
    print('start:', start)
    print('end: ', end)
    print('title_a', title_a_tag)
    return title_a_tag


def check_a_tag(text):
    # print(text[0:20])
    open_par = text.find('(')
    close_par = text.find(')')
    start_a_tag = text.find("<a")
    print('open:', open_par)
    print('close: ', close_par)
    print('start_a: ', start_a_tag)
    if start_a_tag >= 0:
        if (start_a_tag > open_par) and (start_a_tag < close_par):
            print('elif')
            return check_a_tag(text[close_par + 1:]) # mettre return permet de recuperer la variable a la sortie
        if (start_a_tag < open_par) or (start_a_tag > close_par):
            title_a_tag = find_title_a_tag(text[start_a_tag:])
            print('title_a_tag', title_a_tag)
            return title_a_tag
    elif start_a_tag < 0:
        return -1


def find_a_link(soup):
    # list_a = soup.select('p a')
    # for a in list_a:
    #     print(soup.a.parent.name)
    #     print(a)
    list_p = soup.find_all('p')
    for p in list_p:
        # print(p.text)
        # print(str(p))
        str_p = str(p)
        start_a = str_p.find("<a")
        # print(start_a)
        if start_a > 0:
            title_a = check_a_tag(str_p)
            print('road2', title_a)
            return title_a


def roads_to_philosophy(arg):
    url = "https://en.wikipedia.org/wiki/"
    req = requests.get(url+arg)
    if req.status_code != 200:
        print("Error Http request : ", req.status_code)
        exit(0)
    text = req.text
    # print("text :", text)
    soup = BeautifulSoup(text, 'html.parser')
    title = find_title(soup)
    global roads
    if title in roads:
        print("It leads to an infinite loop !")
        exit(0)
    roads.append(title)
    print(title)
    # print(roads)
    if title == 'Philosophy':
        print(format(len(roads)), "roads from ", format(roads[0]), "to Philosophy")
        exit(0)
    road = find_a_link(soup)
    print('road: ', road)
    # roads_to_philosophy(road)


if __name__ == '__main__':
    # if len(sys.argv) < 2:
    #     print("1 argument est demandé")
    #     exit(0)
    # elif len(sys.argv) > 2:
    #     print("1 seul argument est attendu")
    #     exit(0)
    # else:
    #     roads_to_philosophy(sys.argv[1])
    roads_to_philosophy('mathematics')








