#!/usr/bin/env bash
set -e

TOOLS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/tools" && pwd )"

echo "=== Step 1: Activate Python virtual environment ==="
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi
source venv/bin/activate
pip install --upgrade pip
if [ -f "requirements.txt" ]; then
  pip install -r requirements.txt
fi

echo "=== Step 2: Configure PATH for portable JDK and Allure ==="
export PATH="$TOOLS_DIR/jdk/bin:$TOOLS_DIR/allure/bin:$PATH"

echo "✅ Setup completed. You can now run pytest and generate Allure reports."
