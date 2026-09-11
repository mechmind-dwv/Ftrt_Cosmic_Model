#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "=========================================="
echo " FTRT Cosmic Model — Termux Android"
echo "=========================================="

pkg update -y
pkg upgrade -y

pkg install -y \
    git \
    openssh \
    python \
    clang \
    cmake \
    make \
    rust \
    wget \
    curl \
    nano \
    pkg-config \
    libjpeg-turbo \
    libpng \
    freetype

echo
echo "✅ Dependencias de Termux instaladas."
echo
echo "Python:"
python --version

echo
echo "Git:"
git --version

echo
echo "SSH:"
ssh -V 2>&1 | head -n 1

echo
echo "=========================================="
echo " Termux preparado"
echo "=========================================="
