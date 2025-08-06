from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500
    detail = ""


    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)



class UserAlreadyExistsException(BookingException):
    status_code=status.HTTP_409_CONFLICT
    detail="User already exists"


class IncorrectEmailOrPasswordException(BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Incorrect user email or password"


class TokenExpiredException(BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Token expired, please re-login"


class TokenAbsentException(BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Token missing"


class IncorrectFormatTokenException(BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Incorrect format token"


class UserIsNotPresentException(BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED


class RoomCannotBeBookedException(BookingException):
    status_code=status.HTTP_409_CONFLICT
    detail="There are no last places left"