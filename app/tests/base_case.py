import unittest

from flask import current_app as app
from app.main import db


class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass
