import unittest
import json
import requests
from api_crud_book import *

class crud_book_positive(unittest.TestCase):

    new_book_unit = {
    "title": "Tutorial from Unitest",
    "author": "InnaK"}


    def test_crud_book_positive(self):
    #test add book option (check that book with title and author exist)
        id,r_add = add_book(self.new_book_unit)
        self.assertEqual(r_add.status_code,201)
        #self.assertEqual(r_add.json()['title'],"Tutorial from Unitest")
        #self.assertEqual(r_add.json()["author"],"InnaK")
        r = check_book_in_list(id)
        res_check = r.json()
        for i in res_check:
            if i["id"]==id:
                self.assertEqual(i['title'],"Tutorial from Unitest")
                self.assertEqual(i['author'],"InnaK")


