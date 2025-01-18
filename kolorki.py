import matplotlib.pyplot as plt
# import random

# # Generowanie 5 punktów
# points = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(5)]

# # Ustawienie mapy kolorów
# colormap = plt.cm.viridis
# x_values = [point[0] for point in points]

# # Normalizacja wartości x do zakresu 0-1 w celu użycia w kolorach
# normalized_x = [(x - min(x_values)) / (max(x_values) - min(x_values)) for x in x_values]

# # Tworzenie wykresu
# fig, ax = plt.subplots(figsize=(8, 6))

# # Dodawanie punktów w pętli
# for (x, y), norm_x in zip(points, normalized_x):
#     color = colormap(norm_x)  # Pobranie koloru na podstawie znormalizowanej wartości x
#     ax.scatter(x, y, color=color, s=100, edgecolor='black')
#     ax.text(x, y, f"({x:.1f}, {y:.1f})", fontsize=8, ha='right')  # Dodanie etykiety punktu

# # Dodanie paska kolorów dla lepszej wizualizacji zakresu
# sm = plt.cm.ScalarMappable(cmap=colormap, norm=plt.Normalize(vmin=min(x_values), vmax=max(x_values)))
# sm.set_array([])
# fig.colorbar(sm, ax=ax, label="X Value")

# # Etykiety osi
# ax.set_xlabel("X Value")
# ax.set_ylabel("Y Value")
# ax.set_title("Punkty z różnymi kolorami opartymi na wartości X")

# # Wyświetlenie wykresu
# ax.grid(True)
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Przykładowe dane
x = np.linspace(0, 10, 100)
y = np.cos(x)

# Normalizacja danych
normalized = (x - min(x)) / (max(x) - min(x))

# Tworzenie kolorów (od zielonego do czerwonego)
colors = [(1 - norm, norm, 0) for norm in normalized]

# Wykres
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color=colors, s=50)

# Etykiety osi
plt.xlabel("X Value")
plt.ylabel("Y Value")
plt.title("Kolory RGB na podstawie wartości")
plt.grid(True)
plt.show()