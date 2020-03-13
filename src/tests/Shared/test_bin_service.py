import unittest
from Shared import Scheme

class TestBinService(unittest.TestCase):
    def test_scheme_enum(self):
        known_schemes = ['VISA', 'MASTERCARD', 'AMERICAN_EXPRESS', 'CHINA_UNION_PAY']
        for scheme in known_schemes:
            self.assertIsNotNone(Scheme[scheme])


if __name__ == '__main__':
    unittest.main()
