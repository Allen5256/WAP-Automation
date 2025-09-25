# WAP Testing Framework (Pytest + Selenium)

This repository provides a **scalable and maintainable test automation framework** for **WAP (mobile web) testing** using **Selenium + Pytest**. The initial implementation focuses on testing the Twitch mobile web app.

## 🎥 Demo

Here is a GIF showing the test running locally:

![Demo Run](docs/demo.gif)

_(Place your recorded GIF at `docs/demo.gif`. You can create one using tools like [asciinema](https://asciinema.org/), [screen-to-gif](https://www.screentogif.com/), or OBS.)_

---

## 📂 Project Structure

We follow a **Page Object Model (POM)** approach with clear separation of concerns:

- **conftest.py** → Global fixtures, including Selenium WebDriver setup (with Chrome mobile emulator).
- **pages/** → Page Object classes encapsulating locators and page actions.
  - `base_page.py` → Base class with shared logic (WebDriverWait, etc.).
  - `home_page.py` → Methods for homepage interactions.
  - `search_page.py` → Methods for search results interactions.
  - `streamer_page.py` → Methods for streamer page interactions.
- **tests/** → Pytest test cases.
  - `test_twitch_wap.py` → Implements the test scenario.
- **utils/** → Utility functions (e.g., modal handling, screenshot helpers).
- **screenshots/** → Output directory for saved screenshots.
- **requirements.txt** → Python dependencies.
- **pytest.ini** → Pytest configuration.

### Directory Tree

```
wap_test_framework/
├── conftest.py            # Pytest fixtures (driver setup)
├── pages/
│   ├── base_page.py       # Base class
│   ├── home_page.py       # Home page actions
│   ├── search_page.py     # Search page actions
│   └── streamer_page.py   # Streamer page actions
├── tests/
│   └── test_twitch_wap.py # Test case implementation
├── utils/
│   └── helpers.py         # Helper utilities
├── screenshots/           # Screenshots saved here (auto-created)
├── requirements.txt       # Dependencies
├── pytest.ini             # Pytest configuration
└── README.md              # Documentation
```

---

## 🛠️ Prepare for Testing

#### **System prerequisites**
- Python 3.8+
- Google Chrome

#### **Environment setup**

1. **Create a virtual environment**

```bash
python -m venv venv
```

2. **Activate the virtual environment**

- Windows:

```bash
venv\Scripts\activate        # bash

or

.venv\Scripts\Activate.ps1   # powershell
```

- macOS / Linux:

```bash
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Verify pytest is available**

```bash
pytest --version
```

5. **Run tests**

   Simply run `pytest` in the project root for running all reconized tests.

   Note that the framework will automatically discover test files in the tests/ directory that match test\_\*.py.

   You can also specify the test set by using `-k` to pass the test set as the parameter. For example:

```bash
# module level
pytest -k test_twitch_wap.py

# class level
pytest -k TestTwitchWap

# method level
pytest -k test_twitch_select_streamer_and_screenshot
```

#### **Optional: Allure**

   This project uses **Allure** for test reporting. To generate and view reports, you need to have **Allure CLI** installed on your system as one of the the prerequisites.
   Please refer to the official Allure documentation to install it for your operating system: https://docs.qameta.io/allure/

   Note that Installing Allure CLI is **optional**. It is just for generating test reports in a more visual and easy-to-analyze format. If you only want to run the tests for development purposes, having `pytest` installed is sufficient.

  Please follow the steps below to set up Allure (Only take Windows for example here).
  
  1. **Install Allure CLI**
  ```powershell
  
  ```


6. **(Optional) Run in headless mode**

```bash
set HEADLESS=1 # Windows
export HEADLESS=1 # macOS / Linux
pytest tests/
```

---

## ▶️ Demo Test Scenario

The demo test case (`test_twitch_wap.py`) covers:

1. Navigate to [https://m.twitch.tv/](https://m.twitch.tv/)
2. Click the **Browse** icon
3. Search by keyword "**starCraft II**"
4. View all channel/streamer search results
5. Scroll down twice
6. Select the first streamer from the list
7. Wait until the streamer page is fully loaded
8. Handle any popups/modals automatically
9. Take and save a screenshot

---

## 📌 Special Design

- Extend `COMMON_MODAL_CLOSE_SELECTORS` in `utils/helpers.py` for handling new popups.
- Use `pages/` folder to add new Page Objects for better scalability.

---

## 📄 License

MIT License
