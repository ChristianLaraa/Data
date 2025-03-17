import requests
from bs4 import BeautifulSoup

url = 'https://mancandy.mx/collections/all'

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
        print("No se encontraron artículos con la clase 'p'. Revisa la estructura HTML.")
else:
    print(f'Error en la petición {respuesta.status_code}')

promedio = [3800.00, 10200.00, 4400.00, 12800.00, 3600.00, 3800.00, 1800.00, 4400.00, 4100.00, 2800.00, 2400.00, 4800.00,
            12800.00, 3800.00, 2800.00, 4100.00, 2500.00, 3800.00, 4100.00, 4800.00, 12800.00, 5500.00, 4800.00, 6500.00,
            400.00, 8800.00, 4800.00, 3000.00, 4800.00, 3800.00, 5500.00, 12000.00, 5200.00, 2200.00, 4500.00, 8500.00,
            8500.00, 1800.00, 4800.00, 4800.00, 9800.00, 1800.00, 4200.00, 2600.00, 4500.00, 3500.00, 4100.00, 2100.00]
final = sum(promedio) / len(promedio)
print(final)