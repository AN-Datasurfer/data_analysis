import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
np.random.seed(42)
x = np.logspace(0.1, 2, 100)  # Logarithmically spaced values
y = np.random.normal(loc=50, scale=10, size=100)  # Normally distributed y-values
sizes = np.random.uniform(20, 500, size=100)  # Marker sizes
colors = np.random.rand(100)  # Colors mapped to a colormap

# Create scatter plot with all customizations
plt.figure(figsize=(10, 6))  # Set figure size

scatter = plt.scatter(
    x, y,
    s=sizes,                   # Marker size (default: 20)
    c=colors,                  # Marker colors (can be a single color or array)
    cmap='coolwarm',            # Colormap (e.g., 'plasma', 'coolwarm', 'inferno')
    marker='s',                # Marker style (e.g., 's' = square, '^' = triangle)
    alpha=0.7,                 # Transparency (0 = transparent, 1 = opaque)
    edgecolors='black',        # Edge color of markers
    linewidths=1,            # Edge line width
    label="Random Data",       # Label for the legend
    zorder=1                   # Layering order (higher appears on top)
)

# Set axis scales
plt.xscale('linear')  # Options: 'linear', 'log', 'symlog', 'logit'
plt.yscale('log')  # Options: 'linear', 'log', 'symlog', 'logit'

# Axis labels and title
plt.xlabel("X Axis (Log Scale)", fontsize=12)
plt.ylabel("Y Axis (Linear Scale)", fontsize=12)
plt.title("Customized Scatter Plot with plt.scatter()", fontsize=14)

# Add colorbar
cbar = plt.colorbar(scatter)
cbar.set_label("Color Scale")

# Enable grid
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

# Show legend
plt.legend()

# Display plot
plt.show()