from fastapi import Request, Depends
from jose import jwt, JWTError
from datetime import datetime

from app.config import settings
from app.users.dao import UsersDAO
from app.users.models import Users
import app.exceptions as cexceptions

def get_token(request: Request):
    token = request.cookies.get("booking_access_token")

    if not token:
        raise cexceptions.TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except JWTError:
        raise cexceptions.IncorrectFormatTokenException
    expire: str = payload.get("exp")

    if (not expire) or (int(expire) < int(datetime.utcnow().timestamp())):
        raise cexceptions.TokenExpiredException

    user_id: str = payload.get("sub")

    if not user_id:
        raise cexceptions.UserIsNotPresentException

    user = await UsersDAO.find_by_id(int(user_id))

    if not user:
        raise cexceptions.UserIsNotPresentException

    return user


async def get_current_admin_user(current_user: Users = Depends(get_current_user)):
    #if current_user.role != "admin":
       # raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED) 

    return current_user