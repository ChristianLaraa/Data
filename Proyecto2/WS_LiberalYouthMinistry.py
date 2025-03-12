import requests
from bs4 import BeautifulSoup

url = 'https://liberalyouthministry.shop/collections/liberalyouthministry?page=1'

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

promedio = [1600.00, 3300.00, 2300.00, 1100.00, 1800.00, 1800.00, 1800.00, 2800.00, 2800.00, 1100.00, 1100.00, 3000.00,
            3000.00, 1300.00,900.00, 1400.00, 900.00, 2500.00, 2100.00, 2800.00, 2800.00, 3500.00, 1100.00, 1300.00,
            3500.00, 2800.00, 9500.00, 3300.00, 3300.00, 1400.00]
final = sum(promedio) / len(promedio)
print(final)

