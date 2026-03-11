from app.models.diary import Diary
from app.schemas.diary import DiaryCreate, DiaryUpdate
from tortoise.expressions import Q

async def create_diary(user_id: int, data: DiaryCreate):
    diary = await Diary.create(user_id=user_id, **data.dict())
    return diary

async def get_diary(diary_id: int):
    diary = await Diary.get_or_none(id=diary_id) #id로 일기 조회, 없으면 에러 없이 None 반환
    return diary

async def get_diaries(
    user_id: int,
    search: str = None,
    order_by: str = "-created_at", # 최신순, - 빼면 오래된순
    page: int = 1,
    size: int = 10 # 페이징. page는 페이지 번호, size는 페이지당 아이템 수
):

    query = Diary.filter(user_id=user_id)

    if search:
        query = query.filter(
            Q(title__icontains=search) | Q(content__icontains=search)
        )

    diaries = await query.order_by(order_by).offset((page - 1) * size).limit(size)
    return diaries

async def update_diary(diary_id: int, user_id: int, data: DiaryUpdate):
    diary = await Diary.get_or_none(id=diary_id)
    
    if not diary:
        return None
    if diary.user_id != user_id:
        return "forbidden"
    
    update_data = data.dict(exclude_unset=True) # 보낸 값만 업데이트, 안보낸 값은 무시
    await diary.update_from_dict(update_data).save()
    return diary

async def delete_diary(diary_id: int, user_id: int):
    diary = await Diary.get_or_none(id=diary_id)

    if diary is None:
        return None
    if diary.user_id != user_id:
        return "forbidden"
    
    await diary.delete()
    return True