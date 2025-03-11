import requests
from bs4 import BeautifulSoup

url = 'https://crimelife.store/'

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
        print("No se encontraron artículos con la clase 'span'. Revisa la estructura HTML.")
else:
    print(f'Error en la petición {respuesta.status_code}')

## Web Scrapinp para obtener los precios de los productos de la tienda en línea CrimeLifeStore
## Se obtiene el promedio de los precios de la tienda.

## Promedio
# Lista de valores en MXN
valores = [
    1650.00, 1500.00, 1500.00, 1750.00, 1500.00, 1500.00, 1500.00, 1500.00, 1500.00, 1500.00,
    2500.00, 2200.00, 1650.00, 1650.00, 1350.00, 1649.00, 1450.00, 1499.00, 1599.00, 1499.00,
    1599.00, 1750.00, 1349.00, 1349.00
]

# Cálculo del promedio
promedio = sum(valores) / len(valores)
print(promedio)
