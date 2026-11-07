notas = []

while True:
    texto = input("Escriba la nota (o 'fin'): ")

    if texto == "fin":
        break

    try:
        nota = float(texto)
    except ValueError:
        print("❌ Debe ser un número, por ejemplo 4 o 4.5")
        continue

    if not (0 <= nota <= 5):
        print("❌ Debe estar entre 0 y 5")
        continue

    notas.append(nota)

if not notas:
    print("No ingresaste notas")
raise SystemExit
promedio = sum(notas) / len(notas)
print("suma:", sum(notas))
print(f"promedio: {promedio:.2f}")
print("mas alta:", max(notas))
print("mas baja:", min(notas))

if promedio >= 3.0:
    print("Aprobó")
else:
    print("Reprobó")
