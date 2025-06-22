#!/bin/bash

# GitHub Profile Upload Script
# Script untuk mengupload GitHub Profile README ke repository

echo "🚀 GitHub Profile Upload Helper"
echo "================================="
echo ""

# Check if GitHub CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI belum terinstall."
    echo "💡 Install dengan: brew install gh"
    echo "📖 Atau download dari: https://cli.github.com/"
    exit 1
fi

# Check if user is logged in to GitHub CLI
if ! gh auth status &> /dev/null; then
    echo "🔐 Anda belum login ke GitHub CLI."
    echo "💡 Login dengan: gh auth login"
    exit 1
fi

# Get current GitHub username
GITHUB_USERNAME=$(gh api user --jq '.login')
echo "👤 GitHub Username: $GITHUB_USERNAME"
echo ""

# Ask for confirmation
read -p "❓ Apakah username ini benar? (y/n): " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Silakan login dengan akun GitHub yang benar terlebih dahulu."
    echo "💡 Gunakan: gh auth login"
    exit 1
fi

echo "📝 Membuat repository: $GITHUB_USERNAME/$GITHUB_USERNAME"
echo ""

# Create repository (this will be the special profile repository)
gh repo create $GITHUB_USERNAME \
    --public \
    --description "✨ Professional GitHub Profile README - Backend Developer | Laravel Expert | Founder @Aneramedia" \
    --confirm

if [ $? -eq 0 ]; then
    echo "✅ Repository berhasil dibuat!"
else
    echo "⚠️  Repository mungkin sudah ada, melanjutkan dengan push..."
fi

echo ""
echo "📤 Menambahkan remote origin..."

# Add remote origin
git remote add origin https://github.com/$GITHUB_USERNAME/$GITHUB_USERNAME.git

echo "🚀 Pushing files ke GitHub..."

# Push to GitHub
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 SUCCESS! GitHub Profile README berhasil diupload!"
    echo ""
    echo "🔗 Link ke profile Anda:"
    echo "   https://github.com/$GITHUB_USERNAME"
    echo ""
    echo "📋 Langkah selanjutnya:"
    echo "   1. Buka file README.md di repository"
    echo "   2. Edit dan ganti 'fajrunnadhif' dengan '$GITHUB_USERNAME'"
    echo "   3. Update informasi personal sesuai data Anda"
    echo "   4. Test semua links dan pastikan berfungsi"
    echo "   5. Follow checklist di LAUNCH_CHECKLIST.md"
    echo ""
    echo "💡 Pro tip: Gunakan GitHub web editor untuk edit cepat!"
else
    echo "❌ Error saat upload. Cek koneksi internet dan coba lagi."
fi
