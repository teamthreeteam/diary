from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserCreate, UserResponse, TokenResponse
from app.models.user import User
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)
from app.api.dependencies import get_current_user

router = APIRouter()

#회원가입 - Password Hashing 필수
@router.post("/signup", response_model=UserResponse)
async def signup(user_in: UserCreate):
    if await User.filter(email=user_in.email).exists():
        raise HTTPException(status_code=400, detail="이미 가입된 이메일입니다.")

    return await User.create(
        email=user_in.email,
        password=hash_password(user_in.password), # 도구 사용
        nickname=user_in.nickname
    )

#로그인 - JWT Access Token 발급
@router.post("/login", response_model=TokenResponse)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await User.get_or_none(email=form_data.username)

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="아이디 또는 비밀번호가 틀렸습니다.")

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

#내 정보 조회
@router.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    # 이제 검문 로직 없이 깔끔하게 결과만 리턴!
    return current_user