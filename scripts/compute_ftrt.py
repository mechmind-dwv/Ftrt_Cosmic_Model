"""
Compute FTRT index for a given date based on planetary positions
"""
import numpy as np

def ftrt_index(planet_distances_ua, planet_masses_te):
    """
    Calculate relative tidal forces F ≈ M / r^3
    """
    F = planet_masses_te / np.power(planet_distances_ua, 3)
    return F / np.max(F)  # normalize to largest contributor

if __name__ == "__main__":
    # ejemplo: Júpiter y Venus (UA, masa Tierra)
    distances = np.array([5.2, 0.72])
    masses = np.array([317.8, 0.82])
    print("FTRT relativo:", ftrt_index(distances, masses))
