"""
analyze_compare.py
Compara FTRT con índices geomagnéticos (Kp/Dst): calcula correlaciones y genera gráficos.
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

def run(ephem_csv='data/raw/ephem.csv', kp_csv='data/raw/kp_today.csv', ftrt_csv='data/raw/ftrt_daily.csv'):
    f = pd.read_csv(ftrt_csv, parse_dates=['date'])
    k = pd.read_csv(kp_csv, parse_dates=['time_tag'], dayfirst=False)

    # Normaliza columnas según fuente
    k = k.rename(columns={k.columns[0]: 'time_tag', k.columns[1]: 'kp'})
    k['date'] = pd.to_datetime(k['time_tag']).dt.date
    f['date'] = pd.to_datetime(f['date']).dt.date

    merged = pd.merge(f, k[['date', 'kp']], on='date', how='left')
    merged['kp'] = pd.to_numeric(merged['kp'], errors='coerce')
    merged.dropna(subset=['kp'], inplace=True)

    r, p = pearsonr(merged['F_norm'], merged['kp'])
    print(f"🔭 Pearson r = {r:.3f}, p = {p:.3e}")

    plt.figure()
    plt.plot(merged['date'], merged['F_norm'], label='FTRT norm')
    plt.plot(merged['date'], merged['kp'], label='Kp')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('plt/ftrt_vs_kp.png', bbox_inches='tight')
    print("✅ Gráfico guardado: plt/ftrt_vs_kp.png")

if __name__ == '__main__':
    run()
