# Exemplo de Condicionais

valor_pixel = int(input("Informe o valor do pixel: "))

if valor_pixel > 200:
    categoria = "claro"
elif valor_pixel > 100:
    categoria = "médio"
else:
    categoria = "escuro"

print(f"A categoria do pixel é: {categoria}\n")

# Ternário:

valor_pixel_normalizado = valor_pixel / 255.0 if valor_pixel <= 255 else 1.0

print(f"Valor do pixel normalizado: {valor_pixel_normalizado:4f}")