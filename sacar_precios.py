from lxml import html
import requests

page = requests.get('https://www.amazon.es/s?k=kobe+bryant&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=22WMCVFHZEBZE&sprefix=kobe%2Caps%2C625&ref=nb_sb_ss_i_1_4')
tree = html.fromstring(page.content)
print(tree)

# Esto creara la lista de compradores
precio = tree.xpath ('//span[@class="a-price-hole"]/text()')
# Esto creara la lista de precios
producto = tree.xpath('//span[@class="a-text-normal"]/text()')

print('Productos: %s',producto)
print('Precios: %s',precio)

# lxml servira para recorrer el html de la pagina solicitada
# con requests obtenemos el html de una pagina y la almacenamos
# almacenamos en tree su estructura
# en buyers almacenamremos los compradores a traves de los nodos de la web
# prices lo mismo con los precios