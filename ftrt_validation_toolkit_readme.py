"""
Compara FTRT con Kp/Dst: calcula correlaciones y genera gráficos.
"""
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr








def run(ephem_csv='ephem.csv', kp_csv='kp_today.csv', ftrt_csv='ftrt_daily.csv'):
f = pd.read_csv(ftrt_csv, parse_dates=['date'])
k = pd.read_csv(kp_csv, parse_dates=['time_tag'], dayfirst=False)
# normaliza nombres de columnas según la fuente
# Ejemplo: k tiene columnas time_tag, kp
k = k.rename(columns={k.columns[0]:'time_tag', k.columns[1]:'kp'})
k['date'] = pd.to_datetime(k['time_tag']).dt.date
f['date'] = pd.to_datetime(f['date']).dt.date
merged = pd.merge(f.reset_index(), k[['date','kp']], on='date', how='left')
merged['kp'] = pd.to_numeric(merged['kp'], errors='coerce')
merged.dropna(subset=['kp'], inplace=True)
r, p = pearsonr(merged['F_norm'], merged['kp'])
print('Pearson r =', r, 'p =', p)
plt.figure()
plt.plot(merged['date'], merged['F_norm'], label='FTRT norm')
plt.plot(merged['date'], merged['kp'], label='Kp')
plt.legend()
plt.xticks(rotation=45)
plt.savefig('ftrt_vs_kp.png', bbox_inches='tight')
print('Saved ftrt_vs_kp.png')




if __name__ == '__main__':
run()
