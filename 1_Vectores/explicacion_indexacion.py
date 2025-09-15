import numpy as np

# ===== EXPLICACIÓN DETALLADA DE LA INDEXACIÓN [:,1] =====

print("=== ENTENDIENDO LA SINTAXIS [:,1] ===")
print()

# Creamos una matriz de ejemplo
V = np.array([[3, 1],    # Fila 0: [3, 1]
              [2, 4],    # Fila 1: [2, 4]
              [-1, 3]])  # Fila 2: [-1, 3]

print("Matriz V:")
print(V)
print(f"Dimensiones: {V.shape} (3 filas, 2 columnas)")
print()

# ===== DESGLOSANDO LA SINTAXIS [:,1] =====

print("DESGLOSE DE V[:,1]:")
print("• V = nombre de la matriz")
print("• [ ] = operador de indexación")
print("• : = significa 'TODAS las filas'")
print("• , = separador entre filas y columnas")
print("• 1 = índice de la columna (segunda columna, porque se cuenta desde 0)")
print()

# ===== EJEMPLOS PASO A PASO =====

print("=== EJEMPLOS DE INDEXACIÓN ===")
print()

# Todas las filas, columna 0
print("V[:,0] - Todas las filas, columna 0:")
print(f"Resultado: {V[:,0]}")
print("Explicación: Toma TODAS las filas (:) pero solo la columna 0")
print()

# Todas las filas, columna 1
print("V[:,1] - Todas las filas, columna 1:")
print(f"Resultado: {V[:,1]}")
print("Explicación: Toma TODAS las filas (:) pero solo la columna 1")
print()

# ===== COMPARACIÓN CON OTROS TIPOS DE INDEXACIÓN =====

print("=== OTROS EJEMPLOS DE INDEXACIÓN ===")
print()

# Una fila específica, todas las columnas
print("V[0,:] - Fila 0, todas las columnas:")
print(f"Resultado: {V[0,:]}")
print()

print("V[1,:] - Fila 1, todas las columnas:")
print(f"Resultado: {V[1,:]}")
print()

# Un elemento específico
print("V[0,1] - Fila 0, columna 1 (un solo elemento):")
print(f"Resultado: {V[0,1]}")
print()

print("V[2,0] - Fila 2, columna 0 (un solo elemento):")
print(f"Resultado: {V[2,0]}")
print()

# ===== VISUALIZACIÓN DETALLADA =====

print("=== VISUALIZACIÓN DETALLADA ===")
print()
print("Matriz V con índices:")
print("        Col 0  Col 1")
print(f"Fila 0:   {V[0,0]}      {V[0,1]}")
print(f"Fila 1:   {V[1,0]}      {V[1,1]}")
print(f"Fila 2:   {V[2,0]}      {V[2,1]}")
print()

print("V[:,0] extrae la columna 0:")
print(f"[{V[0,0]}, {V[1,0]}, {V[2,0]}] = {V[:,0]}")
print()

print("V[:,1] extrae la columna 1:")
print(f"[{V[0,1]}, {V[1,1]}, {V[2,1]}] = {V[:,1]}")
print()

# ===== ANALOGÍA SIMPLE =====

print("=== ANALOGÍA SIMPLE ===")
print()
print("Piensa en la matriz como una tabla:")
print("• ':' es como decir 'TODAS las filas'")
print("• '1' es como decir 'solo la columna número 1'")
print("• Entonces V[:,1] = 'Dame TODAS las filas, pero solo de la columna 1'")
print()

print("Es como si tuvieras una tabla de Excel y seleccionaras")
print("toda una columna completa (de arriba a abajo)")

# ===== RESUMEN FINAL =====

print("\n=== RESUMEN ===")
print("[:,1] significa:")
print("• : = TODAS las filas (desde la primera hasta la última)")
print("• , = separador")
print("• 1 = columna número 1 (la segunda columna, contando desde 0)")
print("• Resultado: Un array con todos los valores de esa columna")