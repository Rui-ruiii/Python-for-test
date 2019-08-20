#这部分是测试代码

import unittest
from city_country import CountryCity

class CompareTestcase(unittest.TestCase):
    """对照city和country"""

    def test_compare_city_country(self):

        compared_country_and_city = CountryCity('China','Beijing')
        self.assertEqual(compared_country_and_city,'China,Beijing')


if __name__ == '__main__':
    unittest.main()