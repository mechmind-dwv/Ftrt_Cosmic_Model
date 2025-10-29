#!/bin/bash
# 🚀 Script Maestro: Vinculación Cósmica GitHub-Ftrt
# Autor: mechmin-dwv & GPT-5
# Fecha: $(date)
# Propósito: Crear, inicializar y sincronizar el repositorio cósmico con GitHub.

# --- Validación de entorno ---
if [ ! -d ".git" ]; then
    echo "🌀 Inicializando nuevo repositorio Git..."
    git init
else
    echo "✅ Repositorio Git ya existente."
fi

# --- Asegurar rama principal ---
git branch -M main

# --- Añadir y confirmar cambios ---
git add .
git commit -m "🌌 Initial cosmic FTRT model setup"

# --- Conectar remoto (si no existe ya) ---
REMOTE_URL="git@github.com:mechmin-dwv/Ftrt_Cosmic_Model.git"
if ! git remote | grep -q origin; then
    echo "🔗 Conectando con GitHub..."
    git remote add origin "$REMOTE_URL"
else
    echo "🔗 Remoto 'origin' ya configurado."
fi

# --- Sincronizar con el remoto ---
echo "🚀 Enviando commit al universo..."
git push -u origin main || {
    echo "⚠️ Error al hacer push. Verifica acceso SSH o existencia del repo en GitHub."
    exit 1
}

echo "🌠 Sincronización cósmica completada exitosamente."
