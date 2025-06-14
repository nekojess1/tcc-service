from pydantic import BaseModel

class TopicRequest(BaseModel):
    name: str
    number_of_questions: int
    multiple_choice_qty: int
    multiple_choice_options: int
    open_ended_qty: int

class ExerciseRequest(BaseModel):
    topic: TopicRequest
    idiom: str
    difficulty: str
