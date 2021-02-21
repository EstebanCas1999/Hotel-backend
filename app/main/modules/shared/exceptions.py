from werkzeug.exceptions import Unauthorized


class UnauthorizedCredentialsHttpException(Unauthorized):
    pass


class ObjectNotFoundException(Exception):
    """
    Exception thrown when searched for a value and not found
    """
    pass


class InvalidValueError(ValueError):
    """
    Exception thrown when an invalid value has been sent
    """
    pass


class ObjectBadRequestException(Exception):
    """
    Exception thrown when searched for a value and not found
    """


class DuplicateUser(ValueError):
    """
    Exception occurs when the record is duplicated
     """
    pass


class PreconditionFailedException(ValueError):
    """
    Exception occurs when the record is duplicated
     """
    pass


class ConflictException(ValueError):
    """
    Exception occurs when the record is duplicated
     """
    pass
