import unittest
from test_it_employee import it_employee_negative,it_employee_positive

it_tests_pos = unittest.TestSuite()
it_tests_pos.addTest(unittest.makeSuite(it_employee_positive))

it_tests_negative = unittest.TestSuite()
it_tests_negative.addTest(unittest.makeSuite(it_tests_negative))

runner = unittest.TextTestRunner()
runner.run(it_tests_pos)
runner.run(it_tests_negative)
