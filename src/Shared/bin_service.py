from enum import Enum, auto


class Scheme(Enum):
    VISA = auto()
    MASTERCARD = auto()
    AMERICAN_EXPRESS = auto()
    CHINA_UNION_PAY = auto()


class BinService:
    def __init__(self):
        self._schemes = {}
        self._schemes[Scheme.VISA] = "VISA"
        self._schemes[Scheme.MASTERCARD] = "MC"
        self._schemes[Scheme.AMERICAN_EXPRESS] = "AMEX"
        self._schemes[Scheme.CHINA_UNION_PAY] = "CUP"

    def classify_card(self, pan):
        for scheme_enum, scheme_val in self._schemes.items():
            if pan.startswith(scheme_val):
                return scheme_enum
        raise LookupError("Failed to classify card")


