import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 1. Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# 2. Add the base shape (a Circle)
base_circle = patches.Circle((0.5, 0.5), radius=0.3, color='royalblue', alpha=0.6)
ax.add_patch(base_circle)

# 3. Add the polygon on top (a Triangle)
# The vertices of the triangle as an (N, 2) array
triangle_vertices = [[0.5, 0.8], [0.2, 0.2], [0.8, 0.2]]
top_polygon = patches.Polygon(triangle_vertices, closed=True, color='crimson', alpha=0.8)
ax.add_patch(top_polygon)

# 4. Set axis limits and display
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.title("Polygon on Top of Another Shape")
plt.show()