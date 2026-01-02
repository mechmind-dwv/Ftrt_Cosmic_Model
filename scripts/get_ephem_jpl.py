"""
get_ephem_jpl.py
Obtiene efemérides planetarias desde el servicio JPL Horizons (NASA)
para un rango de fechas dado. Guarda resultados en CSV.
"""

import pandas as pd
from datetime import datetime, timedelta
from astroquery.jplhorizons import Horizons
import os

def get_ephem(start_date=None, end_date=None):
    # Si no se pasan fechas, usa últimos 10 días hasta hoy
    if start_date is None or end_date is None:
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=10)

    start_str = start_date.strftime("%Y-%b-%d")
    end_str = end_date.strftime("%Y-%b-%d")

    planets = {
        "Mercury": 1,
        "Venus": 2,
        "Earth": 3,
        "Mars": 4,
        "Jupiter": 5,
        "Saturn": 6,
        "Uranus": 7,
        "Neptune": 8
    }

    rows = []
    for name, pid in planets.items():
        print(f"🔭 Consultando efemérides de {name} ({pid})...")
        obj = Horizons(id=pid, location='@sun', epochs={'start': start_str, 'stop': end_str, 'step': '1d'})
        eph = obj.elements()
        df = eph.to_pandas()
        df['planet'] = name
        for col in ['a', 'e', 'i']:
            if col not in df.columns:
                df[col] = None
        rows.append(df[['datetime_str', 'a', 'e', 'i', 'planet']])

    all_data = pd.concat(rows)
    os.makedirs("data/raw", exist_ok=True)
    all_data.to_csv('data/raw/ephem.csv', index=False)
    print("✅ Efemérides guardadas en data/raw/ephem.csv")

if __name__ == "__main__":
    get_ephem()
