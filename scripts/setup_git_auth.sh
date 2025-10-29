#!/usr/bin/env bash
set -e

echo "🔐 Configuración automática de Git + SSH para GitHub"
echo "==================================================="

EMAIL="ia.mechmind@gmail.com"
USER="mechmind-dwv"
KEY="$HOME/.ssh/id_ed25519"

# 1. Git identity
git config --global user.name "$USER"
git config --global user.email "$EMAIL"

# 2. SSH key
if [ ! -f "$KEY" ]; then
  echo "🔑 Generando clave SSH..."
  ssh-keygen -t ed25519 -C "$EMAIL" -f "$KEY" -N ""
else
  echo "✅ Clave SSH ya existe"
fi

# 3. SSH agent
eval "$(ssh-agent -s)"
ssh-add "$KEY"

# 4. Mostrar clave pública
echo
echo "📌 COPIA ESTA CLAVE EN GITHUB → Settings → SSH keys"
echo "--------------------------------------------------"
cat "${KEY}.pub"
echo "--------------------------------------------------"
echo

# 5. Test conexión
echo "🔍 Probando conexión SSH con GitHub..."
ssh -T git@github.com || true

echo
echo "✅ SSH configurado. Si ves 'You've successfully authenticated', está listo."
