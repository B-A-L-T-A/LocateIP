#Coded by Balta
import time
import requests
from colorama import init, Fore
import os

os.system("clear")

while True:
    print(Fore.BLUE + """
 _                 _       ___ ____  
| | ___   ___ __ _| |_ ___|_ _|  _ \ 
| |/ _ \ / __/ _` | __/ _ \| || |_) |
| | (_) | (_| (_| | ||  __/| ||  __/ 
|_|\___/ \___\__,_|\__\___|___|_|    """)
    print(Fore.YELLOW + "L", end="")
    print(Fore.GREEN + "o", end="")
    print(Fore.BLUE + "c", end="")
    print(Fore.RED + "a", end="")
    print(Fore.CYAN + "t", end="")
    print(Fore.MAGENTA + "e", end="")
    print(Fore.WHITE + "I", end="")
    print(Fore.YELLOW + "P ", end="")
    print(Fore.RED + "V", end="")
    print(Fore.YELLOW + "1", end="")
    print(Fore.GREEN + ".", end="")
    print(Fore.BLUE + "0")

    print(Fore.YELLOW + "C", end="")
    print(Fore.GREEN + "o", end="")
    print(Fore.BLUE + "d", end="")
    print(Fore.RED + "e", end="")
    print(Fore.CYAN + "d ", end="")
    print(Fore.MAGENTA + "b", end="")
    print(Fore.WHITE + "y ", end="")
    print(Fore.YELLOW + "B", end="")
    print(Fore.RED + "a", end="")
    print(Fore.YELLOW + "l", end="")
    print(Fore.GREEN + "t", end="")
    print(Fore.BLUE + "a", end="")
    print(Fore.BLUE + "\n")

    # json: Permite trabajar con la respuesta de la api.
    import json

    # URL de la API
    api_url = "http://ip-api.com/json/"

    # Defini los parametros de respuesta que quiero obtener
    parametros = 'status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query'
    data = {"fields": parametros}


    # Declare la función que se conectara con la API y devolverá la respuesta de la misma.
    def ip_scraping(ip=""):

        # Se conecta con la API
        res = requests.get(api_url + ip, data=data)

        # Se Obtiene y procesa la respuesta JSON
        api_json_res = json.loads(res.content)

        return api_json_res


    if __name__ == '__main__':
        # Solicito la entrada.
        print("""═══════════════════════════
""", end="")
        print(Fore.CYAN + "◈", Fore.WHITE + " Enter the IP address ", Fore.CYAN + "◈")
        print(Fore.BLUE + "╔══════════════════════════")
        ip = input("╚═->>> ")
        print()

        # Llamo a la función ip_scraping y mostro los resultados
        par = parametros.split(",")
        for x in par:
            print(Fore.CYAN + "[+]", x.upper(), "->", ip_scraping(ip)[x])
        time.sleep(3)
