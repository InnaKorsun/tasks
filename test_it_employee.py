import unittest
from ITEmployee import *

class it_employee_positive(unittest.TestCase):

    def setUp(self):
        ## create 3 test instance of ITEmployee class
        self.actual_result = ITEmployee("Victor Petrov",1978,"QA",10,3000)
        self.actual_result_sec = ITEmployee ("Vika Lapina", 1990, "QA", 1, 500)
        self.actual_result_third = ITEmployee("Vitya Lomov", 1990, "QA", 5, 1500)



    def test_it_employee_positive(self):
        self.assertIsInstance(self.actual_result, ITEmployee)
        self.assertIsInstance(self.actual_result, Employee)

    def test_it_employee_add_skill(self):
        #test add skill method(ITEmployee class)
        self.actual_result.add_skill("SQL")
        self.assertListEqual(self.actual_result.skills,["SQL"])

    def tast_it_employee_add_skills(self):
        #test add_skillS method(ITEmployee class)
        self.actual_result.add_skill("Linux","Networking")
        self.assertListEqual(self.actual_result.skills,["Linux","Networking"])



    def test_employee_add_salary(self):
        #test add_salary method((Employee class)
        self.actual_result.raise_salary(1000) ## add salary 1000
        self.assertEqual(self.actual_result.salary, 4000)

    def test_employee_get_name_position(self):
        #test get_bname_position method((Employee class)
        self.assertEqual(self.actual_result.get_name_position(),"Senior QA")
        self.assertEqual(self.actual_result_sec.get_name_position(),"Junior QA")
        self.assertEqual(self.actual_result_third.get_name_position(), "Middle QA")



    def test_person_get_name_surname(self):
        #test get name (Person class)
        self.assertEqual(self.actual_result.get_name(), "Victor")
        #test add_surname method((Person class)
        self.assertEqual(self.actual_result.get_surname(),"Petrov")

    def test_person_get_age_in(self):
        #test age_in method((Person class)
        self.assertEqual(self.actual_result.age_in(2018), 40)


### Negative


            #def test_raise_not_full_name(self):
        #test exception for case: only 1 word in full name)
        #actual_result_negative = ITEmployee("Inna",1990, "QA", 0, 0)
        #with self.assertRaises(Exception) as context:
         #   actual_result_negative
        #actual_result_negative.get_surname()
        #self.assert

    #def test_raise_age(self):
        #test exception for case: year of birth less than 1900)
    #    no_age = self.actual_result_negative.get_year()
    #    print(no_age)
    #    self.assertRaises(Exception,no_age)
    #    pass


if __name__=="__main__":
    unittest.main()
