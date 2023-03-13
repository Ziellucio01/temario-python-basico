# set significa grupo o conjunto
primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)
print(primer | segundo)  # | Union
print(primer & segundo)  # Intersección
print(primer - segundo)  # Diferencia
print(primer ^ segundo)  # Diferencia simetrica


if 5 in segundo:
    print("si se encuentra el 5 en el set")
