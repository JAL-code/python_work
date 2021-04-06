# Python Crash Course: Chapter 11, Eric Matthews, Testing Your Code

import unittest
"""
    To paraphase:
    module unittest is an addon that will test your code
    unit test = verify one specific aspect of a functions input
    test = collection of unit tests
    full coverage = including all possible tests for working
    with a function
    Focus on critical tests, then aim for full coverage.
"""

# import the function to be tested.
from name_function import get_formatted_name

# Name the class with identify the tests with the tested function
class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""

    # self:  the test must inherit from the unittest class.
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        # verify the result matches intended output.
        self.assertEqual(formatted_name, 'Janis Joplin')

     # add new case to test for middle name
    def test_first_middle_last_name(self):
        """Do names like 'Fred Freddy Fredmond' work?"""
        formatted_name = get_formatted_name('fred', 'fredmond', 'freddy')
        # verify the result matches intended output.
        self.assertEqual(formatted_name, 'Fred Freddy Fredmond')

# lets python3 identify this file as the main program.
if __name__ == '__main__':
    # Allows unittest to excute the test code.
    # Add exit=False to prevent none critical SystemExit error.
    unittest.main(exit=False)