import json

from app.tests.base_case import BaseCase


class TestUserRegister(BaseCase):
    def test_successful_register(self):
        name = "Prueba"
        surnames = "Testing"
        document_number = "123456789121243"
        password = "12346"
        payload = json.dumps({"name": name, "surnames": surnames, "documentNumber": document_number,
                              "password": password})
        response = self.app.post('hotel-backend/public/user', headers={"Content-Type": "application/json"},
                                 data=payload)
        self.assertEqual(200, response.status_code)