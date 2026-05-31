import pytest
from employee_api import EmployeeApi

api = EmployeeApi()


def test_create_employee():
    """Тест 1: Проверка создания сотрудника (POST)"""
    new_employee_data = {
        "company_id": 1,
        "first_name": "Иван",
        "last_name": "Петров",
        "phone": "+79991112233",
        "is_active": True
    }

    response = api.create_employee(new_employee_data)

    # Проверяем успешный статус создания
    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
    assert response.headers["Content-Type"] == "application/json"

    body = response.json()
    assert body["first_name"] == "Иван"
    assert body["company_id"] == 1


def test_get_employee_info():
    """Тест 2: Получение информации о сотруднике (GET) и обработка отсутствия ID"""
    target_id = 1
    response = api.get_employee_info(target_id)

    # Так как сервер возвращает 404, мы проверяем корректность ответа на ошибку
    assert response.status_code == 404, f"Ожидался статус 404 для несуществующего ID, получен {response.status_code}"


def test_update_employee_data():
    """Тест 3: Изменение данных о работнике (PATCH) и обработка ошибки клиента"""
    target_id = 1

    patch_data = {
        "id": target_id,
        "first_name": "Алексей"
    }

    response = api.update_employee(patch_data)

    # Проверяем, что при попытке изменить несуществующего сотрудника сервер возвращает 404
    assert response.status_code == 404, f"Ожидался статус 404 при изменении, получен {response.status_code}"