# app/api/dependencies.py

async def get_current_user():
    """
    현재 로그인한 유저를 확인하는 함수입니다.
    지금은 로그인 기능 구현 전이므로, 테스트를 위해 ID가 1인 임시 유저를 반환합니다.
    """
    class TempUser:
        id = 1
        username = "test_user"
        email = "test@example.com"
        
    return TempUser()