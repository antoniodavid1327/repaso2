# calculadora.py

print("--- MI PRIMERA CALCULADORA EN PYTHON ---")

# 1. Pedimos el nombre al usuario
nombre = input("¿Cómo te llamas? ")

# 2. Pedimos dos números (convertimos el texto a número entero con int())
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

# 3. Hacemos la suma
resultado = numero1 + numero2

# 4. Mostramos el resultado en pantalla
print(f"¡Hola {nombre}! La suma de tus números es: {resultado}")
