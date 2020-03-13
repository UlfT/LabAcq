import unittest
from Auth import AuthReciever
from Auth import AuthMessage


class TestAuthReciever(unittest.TestCase):
    def test_init(self):
        reciever = AuthReciever()

    def test_auth(self):
        auth_message = AuthMessage(pan="Visa123", merchant_id=19, ammount=300, timestamp="2020-02-17")
        receiver = AuthReciever()
        self.assertTrue(receiver.authorize(auth_message))

if __name__ == '__main__':
    unittest.main()
