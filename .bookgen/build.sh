#!/bin/bash
# BookGen Build Script
# Simple wrapper to build the documentation

set -e

echo "🚀 BookGen - Building documentation..."

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is required but not found"
    exit 1
fi

# Install markdown if not present
python3 -c "import markdown" 2>/dev/null || {
    echo "📦 Installing required Python package: markdown..."
    pip3 install markdown --break-system-packages || pip3 install markdown --user
}

# Run the generator
python3 .bookgen/generator.py .

echo "✅ Build complete!"
