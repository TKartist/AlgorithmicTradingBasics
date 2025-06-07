import numpy as np
import matplotlib.pyplot as plt

# Parameters
S0 = 100      # initial value
mu = 0.1      # expected return (10%)
sigma = 0.2   # volatility (20%)
T = 1.0       # total time (1 year)
n_steps = 1000
dt = T / n_steps
t = np.linspace(0, T, n_steps)

# Generate Brownian motion
W = np.cumsum(np.sqrt(dt) * np.random.randn(n_steps))
# Solution of GBM
S = S0 * np.exp((mu - 0.5 * sigma**2) * t + sigma * W)

# Plot
plt.plot(t, S)
plt.title("Geometric Brownian Motion")
plt.xlabel("Time")
plt.ylabel("S(t)")
plt.grid(True)
plt.savefig("gbm.png", dpi=500)