"""
get_ephem_jpl.py
Obtiene efemérides planetarias desde el servicio JPL Horizons (NASA)
para un rango de fechas dado. Guarda resultados en CSV.
"""

import sys
import pandas as pd
from astroquery.jplhorizons import Horizons

def get_ephem(start_date, end_date):
    # Lista de planetas a consultar (por sus IDs en JPL)
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
        obj = Horizons(id=pid, location='@sun', epochs={'start': start_date, 'stop': end_date, 'step': '1d'})
        eph = obj.elements()
        df = eph.to_pandas()
        df['planet'] = name
        for col in ['a', 'e', 'i']:
           if col not in df.columns:
              df[col] = None
        rows.append(df[['datetime_str', 'a', 'e', 'i', 'planet']])

    all_data = pd.concat(rows)
    all_data.to_csv('data/raw/ephem.csv', index=False)
    print("✅ Efemérides guardadas en data/raw/ephem.csv")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python scripts/get_ephem_jpl.py YYYY-MM-DD YYYY-MM-DD")
    else:
        get_ephem(sys.argv[1], sys.argv[2])
