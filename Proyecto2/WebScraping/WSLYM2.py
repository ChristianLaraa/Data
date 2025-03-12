import requests
from bs4 import BeautifulSoup

url = 'https://liberalyouthministry.shop/collections/liberalyouthministry?page=2'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

respuesta = requests.get(url, headers=headers)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, 'html.parser')


    print(soup.prettify()[:5000])

    precios = soup.find_all('span', class_='price-item price-item--regular')

    if precios:
        for precio in precios:
            cantidad_precio = precio.get_text(strip=True)
            print(cantidad_precio)
    else:
        print("No se encontraron artículos con la clase 'p'. Revisa la estructura HTML.")
else:
    print(f'Error en la petición {respuesta.status_code}')