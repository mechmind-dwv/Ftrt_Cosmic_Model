#!/bin/bash
# 🌌 FTRT COSMIC PIPELINE AUTOMATOR
# Ejecuta el flujo completo: NOAA → JPL → FTRT → Análisis

echo "========================================"
echo "🌞 Iniciando ciclo cósmico FTRT..."
echo "========================================"
start_time=$(date +%s)

# Activa entorno virtual
source venv/bin/activate

echo "🔭 [1/4] Descargando datos NOAA SWPC (Kp Index)..."
python scripts/get_noaa_swpc.py || { echo "❌ Error en NOAA SWPC"; exit 1; }

echo "🪐 [2/4] Obteniendo efemérides planetarias JPL..."
python scripts/get_ephem_jpl.py 2003-10-20 2003-11-05 || { echo "❌ Error en efemérides JPL"; exit 1; }

echo "⚙️  [3/4] Calculando FTRT relativo..."
python scripts/compute_ftrt.py || { echo "❌ Error en cálculo FTRT"; exit 1; }

echo "📈 [4/4] Analizando correlación FTRT vs Kp..."
python scripts/analyze_compare.py || { echo "❌ Error en análisis"; exit 1; }

end_time=$(date +%s)
elapsed=$((end_time - start_time))

echo "========================================"
echo "✅ Ciclo FTRT completado en $elapsed segundos"
echo "📊 Resultados: plt/ftrt_vs_kp.png"
echo "========================================"