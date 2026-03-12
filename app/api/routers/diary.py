from fastapi import APIRouter, HTTPException, Depends
from app.schemas.diary import DiaryCreate, DiaryUpdate, DiaryResponse
from app.services.diary_service import(
    create_diary,
    get_diary,
    get_diaries,
    update_diary,
    delete_diary
)
from typing import List, Optional

router = APIRouter(prefix="/diaries", tags=["diaries"])

# 일기 작성
@router.post("/", response_model=DiaryResponse)
async def create_diary_route(data: DiaryCreate, user_id: int):
    diary = await create_diary(user_id, data=data)
    return diary

# 일기 목록 조회
@router.get("/", response_model=List[DiaryResponse])
async def get_diaries_route(
    user_id: int,
    search: Optional[str] = None,
    order_by: str = "-created_at",
    page: int = 1,
    size: int = 10
):
    diaries = await get_diaries(
        user_id=user_id,
        search=search,
        order_by=order_by,
        page=page,
        size=size
    )
    return diaries

# 일기 단건 조회
@router.get("/{diary_id}", response_model=DiaryResponse)
async def get_diary_route(diary_id: int):
    diary = await get_diary(diary_id=diary_id)
    if diary is None:
        raise HTTPException(status_code=404, detail="일기를 찾을 수 없습니다.")
    return diary

# 일기 수정
@router.put("/{diary_id}", response_model=DiaryResponse)
async def update_diary_route(diary_id: int, user_id: int, data:DiaryUpdate):
    result = await update_diary(diary_id=diary_id, user_id=user_id, data=data)
    if result is None:
        raise HTTPException(status_code=404, detail="일기를 찾을 수 없습니다.")
    if result == "forbidden":
        raise HTTPException(status_code=404, detail="본인의 일기만 수정할 수 있습니다.")
    return result

# 일기 삭제
@router.delete("/{diary_id}")
async def delete_diary_route(diary_id: int, user_id:int):
    result = await delete_diary(diary_id=diary_id, user_id=user_id)
    if result is None:
        raise HTTPException(status_code=404, detail="일기를 찾을 수 없습니다.")
    if result == "forbidden":
        raise HTTPException(status_code=404, detail="본인의 일기만 삭제할 수 있습니다.")
    return {"message": "삭제가 완료 되었습니다."}