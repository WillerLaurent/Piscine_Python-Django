import requests, json, dewiki, sys


def request_wiki(req):
    req = req.lower()
    r = requests.get(
        "https://fr.wikipedia.org/w/api.php?action=query&titles={}&prop=revisions&rvprop=content&format=json".format(
            req))
    if r.status_code != 200:
        print("Erreur HTTP code :", r.status_code)
        exit(0)
    data = r.json()
    pages = data["query"]["pages"]
    id = ""
    for k in pages:
        id = k
    page = pages[id]
    txt = ""
    if page.get("revisions"):
        revision = page['revisions']
        # print(revision)
        txt = revision[0].get('*')
        if txt.find("#REDIRECT") != -1:
            start = txt.find("[")
            end = txt.find("]")
            sub = txt[(start + 2):end]
            request_wiki(sub)
        else:
            txt = dewiki.from_string(txt)
            file = open("{}.wiki".format(sys.argv[1]), 'w')
            file.write(txt)
            file.close()
    else:
        print("Ce mot est inconnu par Wikipédia!")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Il faut un argument : le nom de la recherche sur wikipedia")
        exit(0)
    else:
        request_wiki(sys.argv[1])
