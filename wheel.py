import matplotlib.pyplot as plt

def draw_divided_circle(num_parts):
    # Create equal fractional weights for each slice
    slices = [1] * num_parts
    
    # Optional styling: alternating or uniform colors
    colors = ['#4CAF50', '#2196F3', '#FFEB3B', '#FF9800', '#9C27B0']
    
    plt.figure(figsize=(6, 6))
    plt.pie(slices, colors=colors[:num_parts] if num_parts <= len(colors) else None, 
            wedgeprops={"edgecolor": "black", "linewidth": 2})
    
    plt.title(f"{num_parts} Possible Outcomes")
    plt.show()

# Visualize a circle split into 7 pieces
draw_divided_circle(7)