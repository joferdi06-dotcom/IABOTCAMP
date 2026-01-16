# Librerias
import re

"""
Espresiones regulares en Python
Problemas Reales
"""

# Codigo
print("Libreria cargada correctamente")

# Ejemplo 1
texto = "Mi nombre es 12345"
resultado = re.search(r"\d+", texto)
print(f"{texto} Resultado {resultado.group()}")
texto = "Mi nombre es 12345-985"
resultado = re.search(r"\d+", texto)
print(resultado.group())
print(f"{texto} Resultado {resultado.group()}")