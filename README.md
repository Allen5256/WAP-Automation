# WAP Testing Framework (Pytest + Selenium)

This repository provides a **scalable and maintainable test automation framework** for **WAP (mobile web) testing** using **Selenium + Pytest**. The initial implementation focuses on testing the Twitch mobile web app.

## 🎥 Demo
Here is a GIF showing the test running locally:

![Demo Run](docs/demo.gif)

*(Place your recorded GIF at `docs/demo.gif`. You can create one using tools like [asciinema](https://asciinema.org/), [screen-to-gif](https://www.screentogif.com/), or OBS.)*

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
### 🛠️ Local Test Execution Guide
1. **Create a virtual environment**
```bash
python -m venv venv
```
2. **Activate the virtual environment**
- Windows:
```bash
venv\Scripts\activate
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
```bash
pytest -q tests/
```
Or simply run `pytest -q` in the project root, the framework will automatically discover test files in the `tests/` directory that match `test_*.py`.

Screenshots will be saved to the `screenshots/` directory.


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
2. Click on the **search** icon
3. Scroll down twice
4. Select the first streamer from the list
5. Wait until the streamer page is fully loaded
6. Handle any popups/modals automatically
7. Take and save a screenshot

---

## 📌 Special Design
- Extend `COMMON_MODAL_CLOSE_SELECTORS` in `utils/helpers.py` for handling new popups.
- Use `pages/` folder to add new Page Objects for better scalability.

---

## 📄 License
MIT License
