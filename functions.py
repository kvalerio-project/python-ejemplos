# Definición de funciones básicas
def hello(name):
    print("hello", name)

hello("sam")
hello("jon")
hello("dante")

# Función que retorna un valor
def add(n1, n2):
    return n1 + n2

print("La suma de 10 y 30 es:", add(10, 30))

def calcular_area_rectangulo(base, altura):
    return base * altura

area = calcular_area_rectangulo(5, 10)
print(f"El área del rectángulo es: {area}")




suma = lambda n1, n2: n1 + n2
print("Resultado lambda:", suma(10, 30))