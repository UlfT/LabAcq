from collections import namedtuple

AuthMessage = namedtuple('AuthMessage', ['pan', 'merchant_id', 'ammount', 'timestamp'])

class AuthReciever:
    def __init__(self):
        pass

    def authorize(self, auth_message):
        # TODO Connect to backends
        return True
