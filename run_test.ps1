Param (
    [string]$target
)

$resultsDir = "allure_results"
$reportDir = "allure_report"

# Accept parameter to specify test set
if ([string]::IsNullOrEmpty($target)) {
    pytest --alluredir=$resultsDir
}
else {
    Write-Output "target (can be module, class or method): $target"
    pytest -k "$target" --alluredir=$resultsDir
}

# Get the exit code of the last command
$test_result = $LASTEXITCODE

# Set to $false if only generate report when there are test failures
$is_always_generate_report = $true

if ($test_result -eq 1 -or $is_always_generate_report) {
    Write-Output "Generate Report Now..."
    allure generate $resultsDir -o $reportDir --clean
    Remove-Item -Recurse -Force $resultsDir

    allure open $reportDir
}
else {
    Remove-Item -Recurse -Force $resultsDir
}
