# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 18:59:40 2024

@author: andre
"""
import matplotlib.pyplot as plt
import numpy as np

# Generar datos
x = np.arange(1, 32)  # 31 categorías en el eje x
y = np.ones((31,))  # 31 valores aleatorios para el eje y

# Definir 31 colores distintivos manualmente
colors = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
    '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5',
    '#c49c94', '#f7b6d2', '#c7c7c7', '#dbdb8d', '#9edae5',
    '#393b79', '#637939', '#8c6d31', '#843c39', '#7b4173',
    '#5254a3', '#8ca252', '#bd9e39', '#ad494a', '#a55194',
    '#6b6ecf'
]

colors2 = [
    '#FF6347', '#4682B4', '#32CD32', '#FFD700', '#6A5ACD',
    '#FF69B4', '#8A2BE2', '#7FFF00', '#D2691E', '#FF4500',
    '#1E90FF', '#ADFF2F', '#FF1493', '#00CED1', '#FF7F50',
    '#7B68EE', '#00FF00', '#DC143C', '#00BFFF', '#FF00FF',
    '#BA55D3', '#CD5C5C', '#4B0082', '#48D1CC', '#C71585',
    '#0000CD', '#FF6347', '#00FA9A', '#8B4513', '#B8860B',
    '#556B2F'
]

colors3 = [
    '#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF',
    '#00FFFF', '#800000', '#808000', '#008000', '#800080',
    '#008080', '#000080', '#FF4500', '#2E8B57', '#DAA520',
    '#4B0082', '#DC143C', '#8B4513', '#5F9EA0', '#D2691E',
    '#FF1493', '#7FFF00', '#FF6347', '#4682B4', '#32CD32',
    '#FFD700', '#6A5ACD', '#FF69B4', '#8A2BE2', '#7FFF00',
    '#C71585'
]

# Crear el gráfico de barras
plt.figure(figsize=(12, 8))
bars = plt.bar(x, y, color=colors3)

# Añadir etiquetas y título
plt.xlabel('Categoría')
plt.ylabel('Valor')
plt.title('Gráfico de Barras Cualitativo con 31 Colores Distintos')

# Añadir etiquetas de categoría
plt.xticks(x, [f'Cat {i}' for i in x], rotation=90)

# Mostrar el gráfico
plt.show()