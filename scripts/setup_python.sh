#!/data/data/com.termux/files/usr/bin/bash
set -e

cd "$(dirname "$0")/.."

echo "=========================================="
echo " FTRT — Entorno Python"
echo "=========================================="

if [ ! -d "venv" ]; then
    echo "🐍 Creando entorno virtual..."
    python -m venv venv
else
    echo "✅ venv ya existe."
fi

source venv/bin/activate

python -m pip install --upgrade pip setuptools wheel

echo
echo "📦 Instalando dependencias compatibles..."

pip install --upgrade --force-reinstall "numpy<2"

pip install --upgrade \
    "pandas>=2.2,<3" \
    "matplotlib>=3.8,<4" \
    "scipy>=1.12,<2" \
    "astroquery>=0.4.10,<1" \
    "requests>=2.31,<3" \
    "jupyter>=1.0,<2" \
    "notebook>=7,<8" \
    "ipykernel>=6,<7"

echo
echo "📌 Guardando entorno:"
pip freeze > requirements.txt

echo
echo "=========================================="
echo " Versiones"
echo "=========================================="

python - <<'PY'
import numpy
import pandas
import matplotlib
import scipy
import astroquery

print("NumPy      :", numpy.__version__)
print("Pandas     :", pandas.__version__)
print("Matplotlib :", matplotlib.__version__)
print("SciPy      :", scipy.__version__)
print("Astroquery :", astroquery.__version__)
PY

echo
echo "=========================================="
echo " ✅ Entorno Python preparado"
echo "=========================================="
