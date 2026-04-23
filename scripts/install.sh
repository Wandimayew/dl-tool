#!/bin/bash

set -e

echo "🚀 Installing DL Tool..."

python3 -m pip install -e .

echo "📦 Checking installation..."
dl --help || echo "❌ Install failed"

echo "✅ Ready to use: dl <url>"

