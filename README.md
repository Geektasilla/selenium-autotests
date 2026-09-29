# Selenium Autotests

Automated UI test suite for [itcareerhub.de](https://itcareerhub.de/ru) built with Python, Selenium and Pytest.

## Coverage

- **Header navigation** — logo, menu links (Programs, About Us, Bildungsgutschein, Reviews, Blog), and language switch buttons are displayed and clickable.
- **Language switch (ru ⇄ de)** — verifies the URL and page heading change correctly when switching languages.
- **About Us → Contacts → Callback flow** — end-to-end navigation scenario that checks the popup text in the callback request form.
- **Payment section screenshot** — a targeted screenshot of a single page section (not the full window).

## Tech Stack

- Python 3
- Selenium WebDriver
- Pytest
- Chrome (the driver is managed automatically via Selenium Manager, no separate driver installation needed)

## Project Structure

```
├── conftest.py              # shared fixtures (driver, driver_on_home_page)
├── tests/
│   ├── test_header_navigation.py
│   ├── test_language_switch.py
│   ├── test_callback_navigation.py
│   └── test_payment_section_screenshot.py
└── screenshots/             # test artifacts
```

## Running the Tests

```bash
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
pip install -r requirements.txt
pytest
```

## Implementation Notes

The "Callback" button in the header is sometimes overlapped by an animated block, which causes a regular Selenium click to be intercepted by another element (`ElementClickInterceptedException`). The fix is a JS-based click via `execute_script`, which targets the element directly in the DOM and bypasses the overlay.
