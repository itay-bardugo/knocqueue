from . import RegistrationStrategy


class RegisterWithCredentialsStrategy(RegistrationStrategy):
    def register(self, subscription):
        self._repository.insert(subscription)
