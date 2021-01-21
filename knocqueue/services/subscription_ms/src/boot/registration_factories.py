from src.factories.registration import RegistrationFactory, CredentialsBuilder

# register factories
factory = RegistrationFactory()
factory.register('credentials', CredentialsBuilder())
