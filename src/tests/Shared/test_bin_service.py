import unittest
from Shared import Scheme
from Shared import BinService

class TestBinService(unittest.TestCase):
    def test_scheme_enum(self):
        known_schemes = ['VISA', 'MASTERCARD', 'AMERICAN_EXPRESS', 'CHINA_UNION_PAY']
        for scheme in known_schemes:
            self.assertIsNotNone(Scheme[scheme])

    def test_classify_card(self):
        bin_service = BinService()
        pans = [("VISA123456", Scheme.VISA), ("MC1911", Scheme.MASTERCARD), ("MC007", Scheme.MASTERCARD),
                ("AMEX711115", Scheme.AMERICAN_EXPRESS), ("CUP9", Scheme.CHINA_UNION_PAY)]
        for pan, true_scheme in pans:
            scheme = bin_service.classify_card(pan)
            self.assertEqual(scheme, true_scheme)

    def test_fail_to_classify_card(self):
        bin_service = BinService()
        pan = "WISA19"
        self.assertRaises(LookupError, bin_service.classify_card, pan)

if __name__ == '__main__':
    unittest.main()
