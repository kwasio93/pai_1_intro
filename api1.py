import urllib.request as ur

try:
    odp = ur.urlopen("https://httpbin.org",timeout=1)
    print("udało się połaczyć")
except:
    print("Nie udało sie polaczyc")
    
