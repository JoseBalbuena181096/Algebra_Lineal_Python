import numpy as np
import matplotlib.pyplot as plt

# Recrear los vectores del notebook
np.random.seed(42)  # Para reproducibilidad
t = np.random.randn(2)
r = np.random.rand(2)

# Calcular la descomposición ortogonal
t_paralelo = r * (np.dot(t, r) / np.dot(r, r))
t_perpendicular = t - t_paralelo

print("Vector objetivo t:", t)
print("Vector de referencia r:", r)
print("Componente paralela t_paralelo:", t_paralelo)
print("Componente perpendicular t_perpendicular:", t_perpendicular)
print("\nVerificación:")
print("t_paralelo + t_perpendicular =", t_paralelo + t_perpendicular)
print("Producto punto t_perpendicular · r =", np.dot(t_perpendicular, r))

# Crear la gráfica
fig, ax = plt.subplots(1, 1, figsize=(10, 8))

# Definir el origen para todos los vectores
origen_x = [0, 0, 0, 0]
origen_y = [0, 0, 0, 0]

# Componentes X e Y de cada vector
vectores_x = [r[0], t[0], t_paralelo[0], t_perpendicular[0]]
vectores_y = [r[1], t[1], t_paralelo[1], t_perpendicular[1]]

# Colores y etiquetas para cada vector
colores = ['blue', 'red', 'green', 'orange']
etiquetas = ['r (referencia)', 't (objetivo)', 't_paralelo', 't_perpendicular']

# Graficar cada vector individualmente
for i in range(4):
    ax.quiver(origen_x[i], origen_y[i], vectores_x[i], vectores_y[i], 
              angles='xy', scale_units='xy', scale=1, 
              color=colores[i], width=0.005, label=etiquetas[i])

# Agregar líneas punteadas para mostrar la descomposición
# Línea desde el extremo de t_paralelo hasta el extremo de t
ax.plot([t_paralelo[0], t[0]], [t_paralelo[1], t[1]], 
        'orange', linestyle='--', alpha=0.7, linewidth=2)

# Línea desde el origen hasta el extremo de t_paralelo
ax.plot([0, t_paralelo[0]], [0, t_paralelo[1]], 
        'green', linestyle=':', alpha=0.7, linewidth=2)

# Configurar la gráfica
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Descomposición Ortogonal de Vectores\nt = t_paralelo + t_perpendicular')
ax.grid(True, alpha=0.3)
ax.legend()
ax.set_aspect('equal')

# Agregar anotaciones
ax.annotate('t', xy=(t[0], t[1]), xytext=(t[0]+0.1, t[1]+0.1), 
            fontsize=12, color='red', weight='bold')
ax.annotate('r', xy=(r[0], r[1]), xytext=(r[0]+0.1, r[1]+0.1), 
            fontsize=12, color='blue', weight='bold')
ax.annotate('t∥', xy=(t_paralelo[0], t_paralelo[1]), 
            xytext=(t_paralelo[0]+0.1, t_paralelo[1]+0.1), 
            fontsize=12, color='green', weight='bold')
ax.annotate('t⊥', xy=(t_perpendicular[0]/2, t_perpendicular[1]/2), 
            xytext=(t_perpendicular[0]/2+0.1, t_perpendicular[1]/2+0.1), 
            fontsize=12, color='orange', weight='bold')

plt.tight_layout()
plt.show()

# Crear una segunda gráfica mostrando paso a paso la construcción
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Construcción Paso a Paso de la Descomposición Ortogonal', fontsize=14)

# Paso 1: Vectores originales r y t
axes[0,0].quiver(0, 0, r[0], r[1], angles='xy', scale_units='xy', scale=1, 
                 color='blue', width=0.005, label='r (referencia)')
axes[0,0].quiver(0, 0, t[0], t[1], angles='xy', scale_units='xy', scale=1, 
                 color='red', width=0.005, label='t (objetivo)')
axes[0,0].set_xlim(-1.5, 1.5)
axes[0,0].set_ylim(-1.5, 1.5)
axes[0,0].set_title('Paso 1: Vectores originales')
axes[0,0].grid(True, alpha=0.3)
axes[0,0].legend()
axes[0,0].set_aspect('equal')

# Paso 2: Agregar componente paralela
axes[0,1].quiver(0, 0, r[0], r[1], angles='xy', scale_units='xy', scale=1, 
                 color='blue', width=0.005, label='r')
axes[0,1].quiver(0, 0, t[0], t[1], angles='xy', scale_units='xy', scale=1, 
                 color='red', width=0.005, label='t')
axes[0,1].quiver(0, 0, t_paralelo[0], t_paralelo[1], angles='xy', scale_units='xy', scale=1, 
                 color='green', width=0.005, label='t_paralelo')
axes[0,1].set_xlim(-1.5, 1.5)
axes[0,1].set_ylim(-1.5, 1.5)
axes[0,1].set_title('Paso 2: Proyección paralela')
axes[0,1].grid(True, alpha=0.3)
axes[0,1].legend()
axes[0,1].set_aspect('equal')

# Paso 3: Agregar componente perpendicular
axes[1,0].quiver(0, 0, r[0], r[1], angles='xy', scale_units='xy', scale=1, 
                 color='blue', width=0.005, label='r')
axes[1,0].quiver(0, 0, t[0], t[1], angles='xy', scale_units='xy', scale=1, 
                 color='red', width=0.005, label='t')
axes[1,0].quiver(0, 0, t_paralelo[0], t_paralelo[1], angles='xy', scale_units='xy', scale=1, 
                 color='green', width=0.005, label='t_paralelo')
axes[1,0].quiver(t_paralelo[0], t_paralelo[1], t_perpendicular[0], t_perpendicular[1], 
                 angles='xy', scale_units='xy', scale=1, 
                 color='orange', width=0.005, label='t_perpendicular')
axes[1,0].plot([t_paralelo[0], t[0]], [t_paralelo[1], t[1]], 
               'orange', linestyle='--', alpha=0.7)
axes[1,0].set_xlim(-1.5, 1.5)
axes[1,0].set_ylim(-1.5, 1.5)
axes[1,0].set_title('Paso 3: Componente perpendicular')
axes[1,0].grid(True, alpha=0.3)
axes[1,0].legend()
axes[1,0].set_aspect('equal')

# Paso 4: Descomposición completa
axes[1,1].quiver(0, 0, r[0], r[1], angles='xy', scale_units='xy', scale=1, 
                 color='blue', width=0.005, label='r')
axes[1,1].quiver(0, 0, t[0], t[1], angles='xy', scale_units='xy', scale=1, 
                 color='red', width=0.005, label='t')
axes[1,1].quiver(0, 0, t_paralelo[0], t_paralelo[1], angles='xy', scale_units='xy', scale=1, 
                 color='green', width=0.005, label='t∥')
axes[1,1].quiver(0, 0, t_perpendicular[0], t_perpendicular[1], angles='xy', scale_units='xy', scale=1, 
                 color='orange', width=0.005, label='t⊥')
# Mostrar que t_paralelo + t_perpendicular = t
axes[1,1].plot([0, t_paralelo[0], t[0]], [0, t_paralelo[1], t[1]], 
               'black', linestyle=':', alpha=0.5, linewidth=2)
axes[1,1].plot([t_paralelo[0], t[0]], [t_paralelo[1], t[1]], 
               'orange', linestyle='--', alpha=0.7, linewidth=2)
axes[1,1].set_xlim(-1.5, 1.5)
axes[1,1].set_ylim(-1.5, 1.5)
axes[1,1].set_title('Paso 4: t = t∥ + t⊥')
axes[1,1].grid(True, alpha=0.3)
axes[1,1].legend()
axes[1,1].set_aspect('equal')

plt.tight_layout()
plt.show()

print("\n=== EXPLICACIÓN DEL PROBLEMA EN EL NOTEBOOK ORIGINAL ===")
print("El problema en tu notebook es que intentas graficar los vectores usando:")
print("plt.quiver(*origen, V[:,0], V[:,1])")
print("\nEsto no funciona correctamente porque:")
print("1. *origen desempaqueta una matriz 2x4, no coordenadas de origen")
print("2. V[:,0] y V[:,1] contienen las componentes X e Y de TODOS los vectores")
print("3. No hay correspondencia correcta entre orígenes y vectores")
print("\nLa solución es graficar cada vector individualmente o usar arrays correctos.")