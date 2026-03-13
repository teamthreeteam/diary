from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.core.config import settings
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="인증 정보가 유효하지 않습니다."
    )

    try:
        #토큰 해독
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        print(f"DEBUG: 토큰에서 추출한 이메일 -> {email}")

        if email is None:
            print("DEBUG: 이메일이 None입니다!")
            raise credentials_exception

    except JWTError as e: # as e 추가
        print(f"DEBUG: JWT 해독 실패! 원인 -> {e}")
        raise credentials_exception

    #DB에서 유저 찾기
    user = await User.get_or_none(email=email)
    if user is None:
        print(f"DEBUG: DB에 {email} 유저가 없습니다!")
        raise credentials_exception

    return user