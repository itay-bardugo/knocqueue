from . import RegistrationStrategy


class RegisterWithCredentialsStrategy(RegistrationStrategy):
    def register(self):
        return 'yes!'
