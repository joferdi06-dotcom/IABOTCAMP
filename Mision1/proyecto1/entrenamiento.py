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
print(f"{texto} Resultado {resultado.group()}")
texto = "Mi nombre es 123*45-985"
resultado = re.findall(r"\d+", texto)
print(f"{texto} Resultado {resultado}")

documento1 = "cc.75.065.60"

def clean_id(documento):
    return re.sub(r"\D",".",documento)
print(clean_id(documento1))