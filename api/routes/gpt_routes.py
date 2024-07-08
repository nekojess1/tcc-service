from fastapi import APIRouter
from api.controllers import (
    feedback_controller,
    mind_map_controller,
    study_guide_controller,
    exercises_controller
)

router = APIRouter()

router.include_router(feedback_controller.router, prefix="/feedback", tags=["Feedback"])
router.include_router(mind_map_controller.router, prefix="/mind-map", tags=["Mind Map"])
router.include_router(study_guide_controller.router, prefix="/study-guide", tags=["Study Guide"])
router.include_router(exercises_controller.router, prefix="/exercises", tags=["Exercises"])
