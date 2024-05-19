# Automated Web Testing with Selenium and pytest

This project contains automated web tests for the website [https://demoqa.com/](https://demoqa.com/) using Selenium and pytest. The tests are designed to be run on both Chrome and Firefox browsers.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

1. Python (version 3.6 or higher)
2. pip (Python package installer)
3. Google Chrome and/or Mozilla Firefox
4. ChromeDriver (for Chrome) and GeckoDriver (for Firefox)

## Installation

1. **Clone the repository:**

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install the required Python packages:**

    ```sh
    pip install -r requirements.txt
    ```

    Ensure `requirements.txt` contains the following (and possibly more as needed):

    ```
    selenium
    pytest
    pytest-html
    webdriver-manager
    ```

3. **Set up WebDriver executables:**

    - **ChromeDriver:**
    - **GeckoDriver:**

## Project Structure
```
/<repository-directory>
├── SCENARIOS
│ ├── __init__.py # Makes SCENARIOS a package
│ ├── main_chrome.py # Contains the test cases for Chrome browser
│ ├── main_firefox.py # Contains the test cases for Firefox browser
│ ├── Test_Scenario_0.py # Contains specific test scenarios
│ ├── Makefile # Contains make commands for running tests and generating reports
│ └── ...
├── LIB_PAGES
│ ├── __init__.py # Makes LIB_PAGES a package
│ ├── general.py # Contains page object models
│ └── ...
└── ...
```
## Usage

### Running Tests

You can run the tests for Chrome and Firefox using the following commands:

- **Run tests on Chrome:**

    ```sh
    make run_chrome
    ```

- **Run tests on Firefox:**

    ```sh
    make run_firefox
    ```

### Generating HTML Reports

Generate HTML reports for Chrome and Firefox using:

- **Generate HTML report for Chrome:**

    ```sh
    make html_report_chrome
    ```

- **Generate HTML report for Firefox:**

    ```sh
    make html_report_firefox
    ```

### Viewing Reports

Open the generated HTML reports using:

- **Open HTML report for Chrome:**

    ```sh
    make open_report_chrome
    ```

- **Open HTML report for Firefox:**

    ```sh
    make open_report_firefox
    ```

### Cleaning Up

Clean up the generated files using:

```sh
make clean
```

## Test Scenario
The following test scenario is automated:

1. Open the website https://demoqa.com/
2. Click on the "Elements" button
3. In the expanded menu, click on "Check Box"
4. Expand the "Home" directory
5. Expand the "Downloads" directory
6. Select the checkbox for "Word File.doc" and verify the selection message
