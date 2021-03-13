class AuthMixinException(Exception):
    pass


class InvalidCredentialException(AuthMixinException):
    pass


class TokenNotProvidedException(AuthMixinException):
    pass
