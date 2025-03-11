import requests
from bs4 import BeautifulSoup

url = 'https://ppaayyss.com/productos/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

respuesta = requests.get(url, headers=headers)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, 'html.parser')


    print(soup.prettify()[:5000])

    precios = soup.find_all('span', class_='js-price-display item-price font-weight-bold')

    if precios:
        for precio in precios:
            cantidad_precio = precio.get_text(strip=True)
            print(cantidad_precio)
    else:
        print("No se encontraron artículos con la clase 'span'. Revisa la estructura HTML.")
else:
    print(f'Error en la petición {respuesta.status_code}')

promedio = [2500.00,2500.00, 2600.00, 500.00, 600.00, 500.00, 350.00, 2500.00, 1000.00, 1999.00, 1999.00, 999.00, 500.00,
            999.00, 500.00, 2400.00, 999.00, 500.00, 999.00, 500.00, 850.00, 2500.00, 1300.00, 1300.00, 2400.00, 2500.00,
            2400.00, 2200.00, 2200.00, 2500.00, 300.00, 300.00, 2200.00, 2500.00, 1200.00, 900.00, 1200.00, 1100.00, 999.00,
            1899.00, 1150.00, 1999.00, 2149.00, 500.00, 2600.00, 500.00, 500.00, 600.00, 400.00, 500.00]
final = sum(promedio) / len(promedio)

print(final)