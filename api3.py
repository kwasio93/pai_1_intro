import requests as ur
import requests.exceptions

N=1
while True:
    try:
        odp = ur.get("https://httpbin.org/delay/2", timeout=N)

        print(f"Udało się połaczyć {N} razy")
    except requests.exceptions.Timeout:
        N=N+1
        print(N)
        
        
