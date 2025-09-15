import numpy as np
import matplotlib.pyplot as plt

# ===== EXPLICACIÓN DETALLADA DE plt.quiver() =====

print("=== 1. ENTENDIENDO EL OPERADOR * (DESEMPAQUETADO) ===")

# Definimos el origen como en tu notebook
origen = np.array([[0], [0]])
print(f"origen = {origen}")
print(f"origen.shape = {origen.shape}")
print(f"origen[0] = {origen[0]} (coordenada X)")
print(f"origen[1] = {origen[1]} (coordenada Y)")

# El operador * desempaqueta los elementos
print("\n¿Qué hace *origen?")
print(f"*origen es equivalente a: origen[0], origen[1]")
print(f"*origen = {origen[0]}, {origen[1]}")
print("Esto separa las coordenadas X e Y del punto de origen")

print("\n=== 2. ENTENDIENDO LA INDEXACIÓN V[:,0] y V[:,1] ===")

# Creamos una matriz V de ejemplo con 3 vectores
V = np.array([[3, 1],    # Vector 1: (3, 1)
              [2, 4],    # Vector 2: (2, 4) 
              [-1, 3]])  # Vector 3: (-1, 3)

print(f"\nMatriz V:")
print(V)
print(f"V.shape = {V.shape} (3 filas, 2 columnas)")

print("\n¿Qué significa V[:,0]?")
print(f"V[:,0] = {V[:,0]} (TODAS las filas, columna 0)")
print("Esto extrae las componentes X de todos los vectores")

print("\n¿Qué significa V[:,1]?")
print(f"V[:,1] = {V[:,1]} (TODAS las filas, columna 1)")
print("Esto extrae las componentes Y de todos los vectores")

print("\n=== 3. VISUALIZACIÓN PASO A PASO ===")

# Explicación visual de cada vector
for i in range(len(V)):
    print(f"Vector {i+1}: desde origen {origen.flatten()} hasta punto ({V[i,0]}, {V[i,1]})")

print("\n=== 4. GRÁFICA COMPLETA ===")

# Crear la gráfica
plt.figure(figsize=(10, 8))

# Graficar los vectores
plt.quiver(*origen, V[:,0], V[:,1], 
           color=['blue', 'red', 'green'], 
           units="xy", scale=1, width=0.005,
           label=['Vector 1', 'Vector 2', 'Vector 3'])

# Añadir etiquetas a cada vector
for i in range(len(V)):
    plt.annotate(f'V{i+1}({V[i,0]}, {V[i,1]})', 
                xy=(V[i,0], V[i,1]), 
                xytext=(V[i,0]+0.3, V[i,1]+0.3),
                fontsize=10, 
                color=['blue', 'red', 'green'][i])

# Marcar el origen
plt.plot(0, 0, 'ko', markersize=8, label='Origen (0,0)')

# Configurar la gráfica
plt.xlim(-3, 5)
plt.ylim(-1, 5)
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Visualización de Vectores con plt.quiver()')
plt.legend()

plt.tight_layout()
plt.show()

print("\n=== RESUMEN ===")
print("• *origen: Separa las coordenadas del punto de inicio")
print("• V[:,0]: Extrae todas las componentes X (columna 0)")
print("• V[:,1]: Extrae todas las componentes Y (columna 1)")
print("• quiver dibuja flechas desde el origen hasta cada punto (X,Y)")