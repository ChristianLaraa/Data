import requests
from bs4 import BeautifulSoup

url = 'https://mitsastudios.com/collections/new-in?page=1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

respuesta = requests.get(url, headers=headers)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, 'html.parser')


    print(soup.prettify()[:5000])

    precios = soup.find_all('span', class_='grid-product__price')

    if precios:
        for precio in precios:
            cantidad_precio = precio.get_text(strip=True)
            print(cantidad_precio)
    else:
        print("No se encontraron artículos con la clase 'p'. Revisa la estructura HTML.")
else:
    print(f'Error en la petición {respuesta.status_code}')

promedio = [3100, 1990, 4850, 4595, 2990, 1990, 1990,  1990, 4850, 4595, 4850, 3595, 2990,3595, 7090, 4850,
            7990, 1990, 4850, 4850, 7090, 7090, 8990, 2990, 3050]
final = sum(promedio) / len (promedio)
print(final)

url = 'https://mitsastudios.com/collections/new-in?page=2'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

respuesta = requests.get(url, headers=headers)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, 'html.parser')


    print(soup.prettify()[:5000])

    precios = soup.find_all('span', class_='grid-product__price')

    if precios:
        for precio in precios:
            cantidad_precio = precio.get_text(strip=True)
            print(cantidad_precio)
    else:
        print("No se encontraron artículos con la clase 'p'. Revisa la estructura HTML.")
else:
    print(f'Error en la petición {respuesta.status_code}')
