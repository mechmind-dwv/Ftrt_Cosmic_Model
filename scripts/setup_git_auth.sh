#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "=========================================="
echo " FTRT — Git / GitHub SSH"
echo "=========================================="

EMAIL="${GIT_EMAIL:-ia.mechmind@gmail.com}"
GITHUB_USER="${GITHUB_USER:-mechmind-dwv}"

git config --global user.email "$EMAIL"
git config --global user.name "$GITHUB_USER"

mkdir -p ~/.ssh
chmod 700 ~/.ssh

KEY="$HOME/.ssh/id_ed25519"

if [ -f "$KEY" ]; then
    echo "✅ Clave SSH existente detectada."
    echo "♻️ Se reutilizará; no se generará otra."
else
    echo "🔐 No existe id_ed25519."
    echo "Generando una nueva clave..."

    ssh-keygen \
        -t ed25519 \
        -C "$EMAIL" \
        -f "$KEY"
fi

eval "$(ssh-agent -s)" >/dev/null 2>&1 || true

ssh-add "$KEY" 2>/dev/null || true

cat > ~/.ssh/config <<CFG
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes
CFG

chmod 600 ~/.ssh/config

echo
echo "=========================================="
echo " 🔑 CLAVE PÚBLICA"
echo "=========================================="
cat "$KEY.pub"

echo
echo "=========================================="
echo " GitHub remoto"
echo "=========================================="

git remote -v || true

echo
echo "🧪 Probando autenticación SSH..."

ssh -T git@github.com || true

echo
echo "=========================================="
echo " IMPORTANTE"
echo "=========================================="
echo
echo "Si GitHub responde:"
echo
echo "Hi $GITHUB_USER! You've successfully authenticated..."
echo
echo "la autenticación SSH funciona."
echo
echo "Si aparece 'Key is invalid', NO generes otra clave."
echo "Copia exactamente el contenido de:"
echo
echo "$KEY.pub"
echo
