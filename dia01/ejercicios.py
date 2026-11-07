# PYTHON 
# ===== Ejercicio 1 =====

nums = [4, 8, 15, 16, 23, 42]

print("Suma:", sum(nums))
print("Máximo:", max(nums))
print("Promedio:", f"{(sum(nums) / len(nums)):.2f}")  

pares = [n for n in nums if n % 2 == 0]
print("Pares:", pares)



# ===== Ejercicio 2 =====
edades = [25, 31, 19]
nombres = ["Ana", "Luis", "Sofía"]
for i, nombre in enumerate(nombres, start=1):
    print(f"{i}. {nombre}")
print(list(zip(nombres, edades)))  # Muestra la relación entre nombres y edades



# ===== Ejercicio 3 =====
edades = [25, 31, 19] 
edad_por_nombre = dict(zip(nombres, edades)) 
print(edad_por_nombre)
print("Edad de Luis:", edad_por_nombre["Luis"])  # Accede a la edad de Luis



# ===== Ejercicio 4 =====
frase = "el perro y el gato y el loro"
conteo = {}

for palabra in frase.split():
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

print(conteo)