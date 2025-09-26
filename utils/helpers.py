import inspect
import os
import time
from pathlib import Path

import allure

SCREENSHOT_DIR = Path("screenshots")
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)


def take_screenshot(driver, prefix="screenshot", folder="screenshots", test_name=None):

    # Find the test function name if not provided
    if not test_name:
        stack = inspect.stack()
        test_name = next((frame.function for frame in stack if frame.function.startswith("test_")), "unknown")

    date_str = time.strftime("%Y%m%d")

    # Ensure the folder exists and create a unique filename by adding an index
    existing = [f for f in os.listdir(folder) if f.startswith(f"{prefix}_{test_name}_{date_str}")]
    index = len(existing) + 1
    filename = f"{prefix}_{test_name}_{date_str}_{index:03d}.png"
    path = os.path.join(SCREENSHOT_DIR, filename)

    driver.save_screenshot(path)

    # Add to Allure report
    with open(path, "rb") as f:
        allure.attach(f.read(), name=filename, attachment_type=allure.attachment_type.PNG)
