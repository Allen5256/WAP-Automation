#!/bin/bash
# -*- coding: UTF-8 -*-
target=$1 # Get the first argument from the command line
if [ "$target" = "" ]; then
        pytest --alluredir=allure_results # If no argument is provided, run tests without a specific target
else
        echo "target (can be module, class or method): $target"
        pytest -k "$target" --alluredir=allure_results # If an argument is provided, run only the specified target
fi
test_result=$?                  # Capture the exit code of the pytest command to decide whether to generate the report
is_always_generate_report=false  # Whether to always generate the report regardless of success; currently set to false (generate only on error)
if [ "$test_result" = "1" ] || [ $is_always_generate_report = true ]; then
        echo "Generate Report Now..."
        allure generate allure_results -o allure-report --clean
        rm -r allure-results

        allure open allure-report
else
        rm -r allure-results
fi
