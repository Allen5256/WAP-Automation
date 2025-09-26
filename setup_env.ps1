Write-Host "=== Step 1: Activate Python virtual environment ==="
if (-Not (Test-Path "venv")) {
    python -m venv venv
}
.\venv\Scripts\Activate.ps1
pip install --upgrade pip
if (Test-Path "requirements.txt") {
    pip install -r requirements.txt
}

Write-Host "=== Step 2: Configure PATH for portable JDK and Allure ==="
$toolsPath = Join-Path $PSScriptRoot "tools"
$env:PATH = "$toolsPath\jdk\bin;$toolsPath\allure\bin;$env:PATH"

Write-Host "✅ Setup completed. You can now run pytest and generate Allure reports."
