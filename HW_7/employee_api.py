import requests

class EmployeeApi:
    BASE_URL = "http://5.101.50.27:8000/employee"

    def create_employee(self, employee_data: dict):
        """1. Создание нового работника (POST)"""
        url = f"{self.BASE_URL}/create"
        response = requests.post(url, json=employee_data)
        return response

    def get_employee_info(self, employee_id: int):
        """2. Получение информации о работнике (GET)"""
        url = f"{self.BASE_URL}/info"
        params = {"id": employee_id}
        response = requests.get(url, params=params)
        return response

    def update_employee(self, updated_data: dict):
        """3. Изменение данных о работнике (PATCH)"""
        url = f"{self.BASE_URL}/change"
        response = requests.patch(url, json=updated_data)
        return response