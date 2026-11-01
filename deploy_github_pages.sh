#!/usr/bin/env bash
set -euo pipefail

export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"
cd "$(dirname "$0")"

REPO_NAME="${1:-ai-benchmark-contradiction-index}"

if ! command -v gh >/dev/null 2>&1; then
  echo "Installing GitHub CLI (gh) via Homebrew..."
  brew install gh
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "Authenticating with GitHub via browser OAuth..."
  (sleep 1 && open "https://github.com/login/device" >/dev/null 2>&1 || true) &
  printf "\n" | gh auth login --hostname github.com --git-protocol https --web --clipboard
fi

# Ensure git uses gh as credential helper for HTTPS pushes
gh auth setup-git --hostname github.com || true

GH_USER="$(gh api user -q .login)"
echo "Authenticated as GitHub user: ${GH_USER}"

if ! git remote get-url origin >/dev/null 2>&1; then
  echo "Creating public repository ${GH_USER}/${REPO_NAME} and pushing main..."
  if ! gh repo create "${REPO_NAME}" --public --source=. --remote=origin --push; then
    git remote add origin "https://github.com/${GH_USER}/${REPO_NAME}.git" 2>/dev/null || \
      git remote set-url origin "https://github.com/${GH_USER}/${REPO_NAME}.git"
    git push -u origin main --force
  fi
else
  echo "Pushing to existing origin..."
  git push -u origin main --force
fi

echo "Enabling GitHub Pages on branch 'main' (root /)..."
gh api -X POST "repos/${GH_USER}/${REPO_NAME}/pages" \
  -f "source[branch]=main" \
  -f "source[path]=/" >/dev/null 2>&1 || \
gh api -X PUT "repos/${GH_USER}/${REPO_NAME}/pages" \
  -f "source[branch]=main" \
  -f "source[path]=/" >/dev/null 2>&1 || true

echo ""
echo "============================================================"
echo "GitHub Pages enabled!"
echo "Repository : https://github.com/${GH_USER}/${REPO_NAME}"
echo "Live Page  : https://${GH_USER}.github.io/${REPO_NAME}/"
echo "Popular    : https://${GH_USER}.github.io/${REPO_NAME}/?view=popular_benchmarks"
echo "All (144)  : https://${GH_USER}.github.io/${REPO_NAME}/?view=ALL"
echo "============================================================"
