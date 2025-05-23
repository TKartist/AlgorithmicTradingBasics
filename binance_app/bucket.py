import pandas as pd
from scipy.stats import gaussian_kde
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("bar_info.csv", index_col="open_time")
df["close_ratio"] = df["close"].pct_change()
df = df.fillna(0)

data = df["close_ratio"].to_numpy()
bins = np.linspace(-0.2, 0.2, 21)  # 21 edges = 20 bins

# Get counts per bin (density=False = raw counts)
counts, bin_edges = np.histogram(data, bins=bins, density=False)

# Bin centers for plotting (optional)
bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

# Put into a DataFrame
hist_df = pd.DataFrame({
    "bin_start": bin_edges[:-1],
    "bin_end": bin_edges[1:],
    "count": counts
})

hist_df.to_csv("density_df.csv", index=False)

plt.bar(bin_centers, np.log1p(counts), width=0.02, edgecolor='black', alpha=0.7)
plt.xlabel("Value Range")
plt.ylabel("Count")
plt.title("Histogram Count in [-0.2, 0.2]")
plt.grid(True)
plt.savefig("price_change_density.png", dpi=500)