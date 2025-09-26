# WAP Testing Framework (Pytest + Selenium)

This repository provides a **scalable and maintainable test automation framework** for **WAP (mobile web) testing** using **Selenium + Pytest**. The initial implementation focuses on testing the Twitch mobile web app.

## 🎥 Demo

#### Here is a GIF showing the test running locally:

<img src="./docs/demo_run.gif" alt="Demo run" style="width:300px;"/>

---

## 📌 Design Principles

- **Separation of Concerns:** Tests focus on validations, while Page Objects encapsulate actions and locators. This keeps the code clean and maintainable.
- **Reusability & Scalability:** Common logic is centralized (e.g., waits, clicks), making it easy to extend the framework for new tests or platforms.
- **Stability with Explicit Waits:** Prioritize `WebDriverWait` with expected conditions over fixed sleeps, ensuring more reliable and faster executions.
- **Configurable Environment:** Driver setup is managed through pytest fixtures, supporting both headless and non-headless modes, and enabling quick environment setup.
- **Transparency on Failures:** Automatic screenshots and optional Allure integration make debugging easier and test results more insightful.

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

## 🛠️ Local Environment Preparation

### **System prerequisites**
- Python 3.8+
- Google Chrome

---

### Preparation steps

**1. Clone & enter the project**
```bash
git clone https://github.com/Allen5256/WAP-Automation.git
cd WAP-Automation
```

---


**2. Download Reporting Tools (JDK + Allure)**

To ensure consistency, please download the **portable (archive) versions** of JDK and Allure according to your operating system.
After downloading, extract them into:

```
project-root/tools/jdk
project-root/tools/allure
```

#### ☕ JDK 11 (LTS) – Portable (Archive)
- 🔗 [Adoptium Temurin 11 Releases](https://adoptium.net/temurin/releases/?version=11)
- Download the **Archive (.zip or .tar.gz)** version for your platform:
  - **Windows** → `OpenJDK11U-jdk_x64_windows_hotspot_<version>.zip`
  - **Linux** → `OpenJDK11U-jdk_x64_linux_hotspot_<version>.tar.gz`
  - **macOS (Intel/Apple Silicon)** → `OpenJDK11U-jdk_x64_mac_hotspot_<version>.tar.gz` or `aarch64` for ARM

#### 📊 Allure CLI – Portable
- 🔗 [Allure CLI GitHub Releases](https://github.com/allure-framework/allure2/releases)
  - Download the latest `allure-<version>.zip` (Windows)

    or

    `allure-<version>.tgz` (Linux/macOS).

---

**3. Configure Python Virtual Environment**

Once the tools are placed in `/tools`, run the provided setup scripts to add them into PATH temporarily for your current session.

#### macOS/Linux
```bash
chmod +x setup_env.sh
./setup_env.sh
```

#### Windows (PowerShell)
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
.\setup_env.ps1
```

👉 These scripts will:
- Create and activate a Python virtual environment.
- Install required Python modules.
- Add `/tools/jdk/bin` and `/tools/allure/bin` to PATH (session only).
- Print the detected Java and Allure versions.

---

**4. Verify Installation**

Activate your Python virtual environment again and check:

#### macOS/Linux
```bash
source venv/bin/activate
java -version
allure --version
```

#### Windows (PowerShell)
```powershell
.venv\Scripts\Activate.ps1
java -version
allure --version
```

✅ Both commands should print version numbers, meaning the environment is ready.

#### ⚠️ Notes
- Do **not** install system-level JDK/Allure unless you prefer managing them manually.
- The `/tools` folder ensures the same JDK and Allure versions are used across all platforms.
- PATH modifications in setup scripts are **temporary for the current shell session** (avoiding system pollution).

---

## ▶️ Run Tests

The test execution script files `run_test.sh` and `run_test.ps1` have already integrated `pytest` + `allure` commands to run the tests. Simply run them in the project root.

#### macOS/Linux
```bash
./run_test.sh
```

#### Windows (PowerShell)
```powershell
.\run_test.ps1
```

Note that the framework will automatically discover test files in the tests/ directory that match `test\_\*.py`.

You can also specify the test set by adding test set name in the command to pass it as the parameter. For example:

```bash
# module level
./run_test.sh test_twitch_wap.py

# class level
./run_test.sh TestTwitchWap

# method level
./run_test.sh test_twitch_select_streamer_and_screenshot
```

---

## ✅ Demo Test Scenario

The demo test case (`test_twitch_wap.py`) covers:

1. Navigate to [https://m.twitch.tv/](https://m.twitch.tv/)
2. Click the **Browse** icon
3. Search by keyword "**starCraft II**"
4. View all channel/streamer search results
5. Scroll down twice
6. Select a random streamer from the list within viewport
7. Handle any popups/modals automatically
8. Wait until the streamer page is fully loaded
9. Take and save a screenshot

---

## 📄 License

MIT License
