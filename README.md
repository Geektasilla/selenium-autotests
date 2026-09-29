# ITCareerHub Selenium Test Suite

Автоматизированные UI-тесты для платформы [itcareerhub.de](https://itcareerhub.de/ru) на Python + Selenium + Pytest.

## Что покрыто

- **Навигация в шапке сайта** — логотип, ссылки меню (Программы, О нас, Bildungsgutschein, Отзывы, Блог), кнопки переключения языка отображаются и кликабельны.
- **Переключение языка (ru ⇄ de)** — проверка смены URL и заголовка страницы при переключении.
- **Переход О нас → Контакты → Обратный звонок** — сквозной сценарий навигации с проверкой всплывающего текста в форме обратного звонка.
- **Скриншот секции "Способы оплаты"** — точечный скриншот конкретного блока страницы (не всего окна).

## Технологии

- Python 3
- Selenium WebDriver
- Pytest
- Chrome (webdriver управляется через Selenium Manager, отдельная установка драйвера не требуется)

## Структура проекта

```
├── conftest.py              # общие фикстуры (driver, driver_on_home_page)
├── tests/
│   ├── test_header_navigation.py
│   ├── test_language_switch.py
│   ├── test_callback_navigation.py
│   └── test_payment_section_screenshot.py
└── screenshots/             # артефакты тестов
```

## Запуск

```bash
python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
pip install -r requirements.txt
pytest
```

## Особенности реализации

Кнопка "Обратный звонок" в хедере иногда перекрывается анимированным блоком, из-за чего обычный Selenium-клик перехватывается посторонним элементом (`ElementClickInterceptedException`). Решение — клик через `execute_script`, который бьёт напрямую по нужному элементу в DOM, в обход перекрывающего слоя.
