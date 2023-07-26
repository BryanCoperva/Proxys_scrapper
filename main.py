import requests


with open("valid_proxies.txt", "r") as f:
    proxies = [linea.strip() for linea in f]
    
site = 'https://cedulaprofesionalsep.online/#Consulta_de_Cedula_Profesional'
counter = 0

for proxy in proxies:
    try:
        print(f"Using the proxy: {proxies[counter]}")
        res = requests.get(site, proxies={"http": proxies[counter],
                                        "https": proxies[counter]})
        print(res.status_code)
    except:
        print("Failed")
    finally:
        counter += 1