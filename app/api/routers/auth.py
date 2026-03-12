from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.user import UserCreate, UserResponse, TokenResponse
from app.models.user import User
from app.core.security import get_password_hash
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import verify_password, create_access_token
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=401, detail="인증 정보가 유효하지 않습니다.")
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = await User.get_or_none(email=email)
    if user is None:
        raise credentials_exception
    return user

router = APIRouter()

@router.post("/signup", response_model=UserResponse)
async def signup(user_in: UserCreate):
    # 1. 이미 가입된 이메일인지 확인
    if await User.filter(email=user_in.email).exists():
        raise HTTPException(status_code=400, detail="이미 가입된 이메일입니다.")

    # 2. 비밀번호 암호화해서 유저 생성
    user = await User.create(
        email=user_in.email,
        hashed_password=get_password_hash(user_in.password),
        nickname=user_in.nickname
    )
    return user

@router.post("/login", response_model=TokenResponse)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    #유저 찾기
    user = await User.get_or_none(email=form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="아이디 또는 비밀번호가 틀렸습니다.")

    #비밀번호 검증
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="아이디 또는 비밀번호가 틀렸습니다.")

    #토큰 생성 및 발급
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    #현재 로그인한 유저 정보 반환
    return current_user