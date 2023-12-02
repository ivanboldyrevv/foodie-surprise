import unittest
from data_parser.parser import *

from database import Database


class ParserTests(unittest.TestCase):
    def test_parse_existing_category(self):
        parse_obj = PageParser()
        parse_obj.category = 'zakuski'
        self.assertIsInstance(parse_obj.get_parse_data_from_soup(), dict)


class DatabaseTests(unittest.TestCase):
    db_obj = Database()

    def test_get_category(self):
        self.assertIsNotNone(self.db_obj.get_recipes_by_category(1))
        test_get_category = self.db_obj.get_recipes_by_category(1)
        test_get_category2 = self.db_obj.get_recipes_by_category(1)
        self.assertNotEquals([recipe['recipe_name'] for recipe in test_get_category],
                             [recipe['recipe_name'] for recipe in test_get_category2])


if __name__ == '__main__':
    unittest.main()
