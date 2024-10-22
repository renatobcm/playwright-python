# Playwright Login Tests

This project contains automated tests to validate the login functionality of the Test Assessment page [https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/](https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/) using the Playwright framework.

## Pre-requisites

- Python 3.x installed
- Pip installed

## Installation

1. Clone the repository:
   ```
   git clone <repo-url>
   cd playwright__tests
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   playwright install
   ```

## Running Tests

To run the tests, use the following command:

```
pytest
```

To run the tests with a detailed HTML report, use:

```
pytest --html=report.html
```

## Reports

After running the tests with the `--html` option, a `report.html` file will be generated in the project's root directory. This report contains detailed information about the executed tests, including:

- Test summary (passed/failed/skipped)
- Details of each test case
- Screenshots (if configured) - TBD
- Console logs

To view the report, open the `report.html` file in a web browser.

## Project Structure

- `tests/`: Directory containing test files
- `pages/`: Directory containing Page Object classes
- `conftest.py`: pytest configuration file
- `requirements.txt`: List of project dependencies

## Contributing

To contribute to the project, please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add some NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request