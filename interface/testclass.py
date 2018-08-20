from .client import Client
from database.db import Db
import unittest


class TestCase(unittest.TestCase):

    def setUp(self, client='Client', db='Db'):

        self.client=Client.read_config(client)
        self.db=Db.read_config(db)