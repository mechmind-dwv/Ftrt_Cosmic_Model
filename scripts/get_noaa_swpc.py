"""
get_noaa_swpc.py
Descarga datos de índice Kp desde NOAA SWPC y los guarda como CSV.
"""

import requests
import pandas as pd

def get_kp_data(output='data/raw/kp_today.csv'):
    url = 'https://services.swpc.noaa.gov/json/planetary_k_index_1m.json'
    print(f"🔭 Descargando datos desde {url}")
    
    r = requests.get(url, timeout=10)
    r.raise_for_status()

    data = r.json()
    df = pd.DataFrame(data)
    df.to_csv(output, index=False)
    print(f"✅ Datos Kp guardados en {output}")

if __name__ == '__main__':
    get_kp_data()
