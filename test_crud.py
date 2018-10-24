import unittest
import json
import requests
from api_crud_book import *

class crud_book_positive(unittest.TestCase):

    new_book = {
    "title": "Tutorial from Unitest",
    "author": "InnaK"
}
    #def setUp(self):
        ## create 3 test instance of ITEmployee clasa


    def test_crud_book_positive(self):
        id = add_book(new_book)
        self.assertEqual()
