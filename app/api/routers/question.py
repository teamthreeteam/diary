from fastapi import APIRouter, HTTPException, Depends
from app.models.reflection import Reflection
from app.models.userquestionhistory import UserQuestionHistory
from app.core.security import get_current_user
from app.schemas.question import QuestionResponse

router = APIRouter(prefix="/questions", tags=["questions"])

@router.get("/random", response_model=QuestionResponse)
async def get_random_question(current_user=Depends(get_current_user)):
    # 1. DB에서 랜덤 질문 1개 조회
    question = await Reflection.all().order_by("?").first()

    if not question:
        raise HTTPException(status_code=404, detail="질문이 없습니다")

    # 2. UserQuestionHistory에 이력 저장
    history = await UserQuestionHistory.create(
        user=current_user,
        question=question,
    )

    # 3. 응답 반환
    return {
        "user_question_id": history.id,
        "question": question.question_text
    }
