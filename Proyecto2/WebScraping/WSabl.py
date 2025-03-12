import requests
from bs4 import BeautifulSoup

url = 'https://www.abl-estudio.com/collections/ropa'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

respuesta = requests.get(url, headers=headers)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, 'html.parser')


    print(soup.prettify()[:5000])

    precios = soup.find_all('p', class_='grid-link__meta')

    if precios:
        for precio in precios:
            cantidad_precio = precio.get_text(strip=True)
            print(cantidad_precio)
    else:
        print("No se encontraron artículos con la clase 'span'. Revisa la estructura HTML.")
else:
    print(f'Error en la petición {respuesta.status_code}')

promedio = [5990.00, 5000.00, 3300.00, 5690.00, 6150.00, 1180.00, 5980.00, 6880.00,  1180.00, 1180.00, 2300.00, 5660.00,
            6650.00,  6600.00, 4700.00, 2500.00, 4980.00, 9700.00, 4530.00, 2900.00, 5365.39, 11000.00, 5300.00, 1105.00,
            6800.00, 2750.00, 6340.00, 5850.00, 13345.00, 6340.00, 6020.00, 19199.00, 2900.00, 5000.00, 2800.00, 2500.00,
            1780.00, 4800.00, 3700.00, 4032.44]
final = sum(promedio)/len(promedio)
print(final)