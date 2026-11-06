nums = [4, 8, 15, 16, 23, 42]

print("Suma:", sum(nums))
print("Máximo:", max(nums))
print("Promedio:", f"{(sum(nums) / len(nums)):.2f}")  

pares = [n for n in nums if n % 2 == 0]
print("Pares:", pares)