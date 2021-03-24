import json

from app.tests.base_case import BaseCase


class TestUserLogin(BaseCase):
    def test_successful_login(self):
        document = "123456789"
        password = "12346"
        payload = json.dumps({"documentNumber": document, "password": password})
        response = self.app.post('hotel-backend/public/auth', headers={"Content-Type": "application/json"},
                                 data=payload)
        self.assertEqual(200, response.status_code)