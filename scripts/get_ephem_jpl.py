"""
Descarga efemérides desde JPL HORIZONS mediante astroquery.
Salida: CSV con columnas: date(UTC), target, lon_deg, lat_deg, distance_au
"""
from astroquery.jplhorizons import Horizons
import pandas as pd
from datetime import datetime, timedelta


TARGETS = {
'Mercury': 199,
'Venus': 299,
'Earth': 399,
'Mars': 499,
'Jupiter': 599,
'Saturn': 699,
'Uranus': 799,
'Neptune': 899,
'Pluto': 999
}


def fetch_range(start, end, step_days=1):
dates = []
d = start
while d <= end:
dates.append(d.strftime('%Y-%m-%d'))
d += timedelta(days=step_days)
return dates




def query_targets(dates, out_csv='ephem.csv'):
rows = []
for tname, tid in TARGETS.items():
print(f'Querying {tname}...')
obj = Horizons(id=tid, location='@sun', epochs=[d for d in dates])
eph = obj.elements()
# columns: datetime_jd, incl, omg, w, a, ecc, meanAnom, longAscNode, argPeri, hlon, hlat, r
# We'll use helio. longitude (hlon) and r (distance AU)
for i, d in enumerate(dates):
try:
lon = float(eph['HLON'][i])
lat = float(eph['HLAT'][i])
r = float(eph['R'][i])
except Exception as e:
lon, lat, r = None, None, None
rows.append({'date': d, 'target': tname, 'lon_deg': lon, 'lat_deg': lat, 'distance_au': r})
df = pd.DataFrame(rows)
df.to_csv(out_csv, index=False)
print('Saved', out_csv)


if __name__ == '__main__':
import sys
if len(sys.argv) < 3:
print('Usage: python get_ephem_jpl.py YYYY-MM-DD YYYY-MM-DD [step_days]')
sys.exit(1)
start = datetime.fromisoformat(sys.argv[1])
end = datetime.fromisoformat(sys.argv[2])
step = int(sys.argv[3]) if len(sys.argv) > 3 else 1
dates = fetch_range(start, end, step)
query_targets(dates)
