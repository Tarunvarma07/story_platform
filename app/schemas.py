
from pydantic import BaseModel

class StoryCreate(BaseModel):
    title: str
    content: str
    author: str