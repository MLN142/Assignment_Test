import numpy as np
import matplotlib.pyplot as plt

def translate(points, tx, ty):

    translation_matrix = np.array([[1, 0, tx], 
                                   [0, 1, ty], 
                                   [0, 0, 1]])  


    ones = np.ones((points.shape[0], 1))
    homogeneous_points = np.hstack([points, ones])

    translated_points = np.dot(homogeneous_points, translation_matrix.T)

    return translated_points[:, :2]  


num_points = int(input("Enter the number of points in the shape: "))
points = []
for i in range(num_points):
    x, y = map(float, input(f"Enter coordinates of point {i+1} (x y): ").split())
    points.append((x, y))
points.append(points[0])  


points = np.array(points)


num_translations = int(input("Enter the number of translations: "))
translations = []
for i in range(num_translations):
    tx, ty = map(float, input(f"Enter translation {i+1} (tx ty): ").split())
    translations.append((tx, ty))


translated_shapes = [points]
for tx, ty in translations:
    new_points = translate(translated_shapes[-1], tx, ty)
    translated_shapes.append(new_points)


plt.figure(figsize=(8, 6))
colors = ['b', 'g', 'r', 'c', 'm', 'y']  
labels = ["Original"] + [f"Translation {i+1}" for i in range(len(translations))]

for shape, color, label in zip(translated_shapes, colors, labels):
    plt.plot(shape[:, 0], shape[:, 1], marker='o', linestyle='-', color=color, label=label)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)
plt.title("Composite 2D Translation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
