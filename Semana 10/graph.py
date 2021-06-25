n = int(input("Ingrese el número de Países: "))
print("Ingresa los países con sus vecinos")
def crear_diccionario():
  d = {}
  x = 0

  while x <n:
    clave = input("País:")
    valor = input("Vecinos:").split(" ")
    d[clave] = valor
    x += 1
  return d


conexiones = crear_diccionario()
print(conexiones)

PO = input("Ingrese pais origen")
PD = input("País destino")


conexiones = {'Peru': ['Brazil'], 'Venezuela': ['Brazil'], 'Brazil': ['Peru', 'Venezuela']}

visitados = [False] * len(conexiones)
def hallar_ruta(mapa,origen,destino):
    queue = [[origen]]
    while len(queue) > 0:
        path = queue.pop(0)
        node = path[-1]
        if node == destino:
            return path
        for adjacent in mapa.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
ruta = hallar_ruta(conexiones,PO,PD)
print(f"Se pasará por {len(ruta)} paises")
print("Los paises son:", end=" ")
for i in ruta:
    if i == ruta[-2]:
        print(i,end=" y ")
    elif i == ruta[-1]:
        print(i,end=".")
    else:
        print(i, end=", ")
