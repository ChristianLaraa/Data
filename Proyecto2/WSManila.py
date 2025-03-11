import requests
from bs4 import BeautifulSoup

url = 'https://maisonmanila.com/collections/essentials'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

respuesta = requests.get(url, headers=headers)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, 'html.parser')


    print(soup.prettify()[:5000])

    precios = soup.find_all('span', class_='money')

    if precios:
        for precio in precios:
            cantidad_precio = precio.get_text(strip=True)
            print(cantidad_precio)
    else:
        print("No se encontraron artículos con la clase 'span'. Revisa la estructura HTML.")
else:
    print(f'Error en la petición {respuesta.status_code}')

promedio = [1450.00,3400.00, 1450.00, 3400.00, 3400.00, 3400.00, 1900.00, 1900.00, 1450.00, 1900.00, 3400.00, 3400.00,
            3400.00, 3400.00]
final = sum(promedio)/len(promedio)
print(final)