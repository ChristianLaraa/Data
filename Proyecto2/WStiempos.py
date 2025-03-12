import requests
from bs4 import BeautifulSoup

url = 'https://tiempos.shop/shop/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

respuesta = requests.get(url, headers=headers)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, 'html.parser')


    print(soup.prettify()[:5000])

    precios = soup.find_all('p', class_='precio')

    if precios:
        for precio in precios:
            cantidad_precio = precio.get_text(strip=True)
            print(cantidad_precio)
    else:
        print("No se encontraron artículos con la clase 'p'. Revisa la estructura HTML.")
else:
    print(f'Error en la petición {respuesta.status_code}')

promedio = [5800.00, 6000.00, 7900.00, 1500.00, 1500.00, 1500.00, 1500.00, 1500.00, 1500.00, 9500.00, 6500.00, 5000.00,
            3700.00, 9000.00, 9500.00, 5000.00, 5000.00, 5000.00, 4500.00, 3000.00, 3000.00, 19500.00, 19500.00, 19500.00]
promedioFinal= sum (promedio) / len (promedio)
print(promedioFinal)
