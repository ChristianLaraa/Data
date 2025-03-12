import requests
from bs4 import BeautifulSoup

url = 'https://hypebeast.com/tags/mexico'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

respuesta = requests.get(url, headers=headers)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, 'html.parser')


    print(soup.prettify()[:5000])

    articulos = soup.find_all('a', class_='title')

    if articulos:
        for articulo in articulos:
            nombre_articulo = articulo.get_text(strip=True)
            print(nombre_articulo)
    else:
        print("No se encontraron artículos con la clase 'title'. Revisa la estructura HTML.")
else:
    print(f'Error en la petición {respuesta.status_code}')
