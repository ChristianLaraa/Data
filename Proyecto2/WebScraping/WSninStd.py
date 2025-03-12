import requests
from bs4 import BeautifulSoup

url = 'https://ninstudio.org/collections/fw24-collection'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

respuesta = requests.get(url, headers=headers)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, 'html.parser')


    print(soup.prettify()[:5000])

    precios = soup.find_all('p', class_='price')

    if precios:
        for precio in precios:
            cantidad_precio = precio.get_text(strip=True)
            print(cantidad_precio)
    else:
        print("No se encontraron artículos con la clase 'p'. Revisa la estructura HTML.")
else:
    print(f'Error en la petición {respuesta.status_code}')

promedio = [198.00,228.00,190.00,215.00,140.00,130.00,192.00,173.00,162.00,225.00,250.00,120.00,298.00,336.00,295.00,330.00,
            340.00,460.00,340.00,336.00,264.00,398.00,565.00,306.00,495.00,180.00, 130.00]
final = sum(promedio) / len(promedio)
print(final)

dolar = 20.37
finalmxn = final * dolar
print(finalmxn)