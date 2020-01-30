from lxml import html
import requests

page = requests.get("http://gurizone.local/catalogo")
tree = html.fromstring(page.content)

# Esto creara la lista de compradores
producto = tree.xpath ('//h3/a/text()')
# Esto creara la lista de precios
precio = tree.xpath('//p[contains(@class,"font-weight-bold")]/text()')
for i in range(len(producto)):
    print('El producto '+producto[i]+' cuesta '+precio[i])

# lxml servira para recorrer el html de la pagina solicitada
# con requests obtenemos el html de una pagina y la almacenamos
# almacenamos en tree su estructura
# en buyers almacenamremos los compradores a traves de los nodos de la web
# prices lo mismo con los precios