import requests
from bs4 import BeautifulSoup

url = 'https://filia.store/collections/todo#'

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

promedio = [1200.00, 1250.00, 1900.00, 1900.00, 5500.00, 990.00, 3853.00, 3855.00, 4640.00, 5990.00, 5990.00, 5990.00,
            3490.00, 3490.00, 3490.00, 10830.00, 2850.00, 4385.00, 9130.00, 3105.00, 1800.00, 2520.00, 4320.00, 2160.00]
final = sum(promedio) / len(promedio)
print(final)