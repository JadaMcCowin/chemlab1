#Thiscodeproducesthebargraphforthemeasurementslab
import matplotlib.pyplot as plt
import numpy as np

# Trial data
measurements = ['measurement 1', 'measurement 2', 'measurement 3', 'measurement 4', 'measurement 5']
densities = [0.6, 0.9, 0.9, 0.1, 1.0]  # g/mL
true_density = 1.0  # g/mL

# Calculations
mean_density = np.mean(densities)  # 0.70 g/mL
std_density = np.std(densities, ddof=1)  # 0.37 g/mL

# Plot setup
plt.figure(figsize=(8, 5))
colors = ['#4C72B0', '#55A868', '#C44E52', '#8172B2', '#CCB974']
bars = plt.bar(measurements, densities, color=colors, width=0.45, edgecolor='black', alpha=0.85)

# Value annotations on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.03,
             f'{height:.1f} g/mL', ha='center', va='bottom', fontweight='bold', fontsize=9.5)

# Horizontal lines for Average and True Density
plt.axhline(y=mean_density, color='crimson', linestyle='--', linewidth=2,
            label=f'Average ({mean_density:.2f} g/mL)')
plt.axhline(y=true_density, color='purple', linestyle=':', linewidth=2,
            label=f'True Density ({true_density:.1f} g/mL)')

# Vertical Standard Deviation Error Bar
plt.errorbar(x=2, y=mean_density, yerr=std_density, fmt='none',
             ecolor='darkred', elinewidth=2.5, capsize=6, capthick=2,
             label=f'SD (±{std_density:.2f} g/mL)')

# Formatting
plt.title('Density of water at 18 C in a graduated cylinder', fontsize=12, fontweight='bold', pad=12)
plt.ylabel('Density (g/mL)', fontsize=11)
plt.ylim(0, 1.6)
plt.legend(loc='upper left', frameon=True)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Trial data for Graph 2 (Updated)
measurements = ['measurement 1', 'measurement 2', 'measurement 3', 'measurement 4']
densities = [1.0, 0.1, 0.1, 1.1]  # g/mL
true_density = 1.0  # g/mL

# Calculations
mean_density = np.mean(densities)  # 0.575 g/mL
std_density = np.std(densities, ddof=1)  # 0.550 g/mL

# Plot setup
plt.figure(figsize=(8, 5))
colors = ['#4C72B0', '#55A868', '#C44E52', '#8172B2']
bars = plt.bar(measurements, densities, color=colors, width=0.45, edgecolor='black', alpha=0.85)

# Value annotations on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.03,
             f'{height:.1f} g/mL', ha='center', va='bottom', fontweight='bold', fontsize=9.5)

# Horizontal reference lines
plt.axhline(y=mean_density, color='crimson', linestyle='--', linewidth=2,
            label=f'Average ({mean_density:.3f} g/mL)')
plt.axhline(y=true_density, color='purple', linestyle=':', linewidth=2,
            label=f'True Density ({true_density:.1f} g/mL)')

# Vertical Standard Deviation Error Bar on Average line
plt.errorbar(x=1.5, y=mean_density, yerr=std_density, fmt='none',
             ecolor='darkred', elinewidth=2.5, capsize=6, capthick=2,
             label=f'SD (±{std_density:.2f} g/mL)')

# Formatting
plt.title('Graph 2: Density of water at 22 C with a beaker', fontsize=12, fontweight='bold', pad=12)
plt.ylabel('Density (g/mL)', fontsize=11)
plt.ylim(0, max(densities) + 0.5)
plt.legend(loc='upper left', frameon=True)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()