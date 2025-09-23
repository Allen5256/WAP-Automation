import time
from datetime import datetime
from pathlib import Path
from selenium.webdriver.common.by import By

SCREENSHOT_DIR = Path("screenshots")
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

COMMON_MODAL_CLOSE_SELECTORS = [
    "button[aria-label='Close']",
    "button[aria-label='Dismiss']",
    "button[data-a-target='modal-close']",
    ".tw-modal__close",
    ".close",
    "button[title='Close']",
]

def take_timestamped_screenshot(driver, name_prefix: str = "screenshot") -> Path:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = SCREENSHOT_DIR / f"{name_prefix}_{ts}.png"
    driver.save_screenshot(str(filename))
    return filename

def close_known_modals(driver):
    for sel in COMMON_MODAL_CLOSE_SELECTORS:
        elems = driver.find_elements(By.CSS_SELECTOR, sel)
        for e in elems:
            if e.is_displayed():
                try:
                    e.click()
                except Exception:
                    try:
                        driver.execute_script("arguments[0].click();", e)
                    except Exception:
                        pass
                time.sleep(0.5)
