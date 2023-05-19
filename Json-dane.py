import urllib.request as ur
import json
import jmespath

url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"
odp = ur.urlopen(url)
str_odp=odp.read().decode("utf-8")
odp.close()
js=json.loads(str_odp)
nazwa = (js["members"])
for i in nazwa:
    print(i["name"])

for j in range(0,len(nazwa)):
    szukaj_nazwy = f"members[{j}].name"
    print(jmespath.search(szukaj_nazwy,js))
    
