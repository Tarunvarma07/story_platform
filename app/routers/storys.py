from fastapi import APIRouter
router = APIRouter()
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Story
from schemas import StoryCreate

router = APIRouter()

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import get_db


@router.post("/stories")
def create_story(
    story: StoryCreate,
    db: Session = Depends(get_db)
):

    new_story = Story(
        title=story.title,
        content=story.content,
        author=story.author
    )

    db.add(new_story)

    db.commit()

    db.refresh(new_story)

    return new_story

@router.get("/stories")
def get_stories(db: Session = Depends(get_db)):

    stories = db.query(Story).all()

    return stories

@router.get("/stories/{id}")
def get_story(id: int,db: Session = Depends(get_db)):

    story = db.query(Story).filter(Story.id == id).first()

    return story




@router.put("/stories/{id}")
def update_story(id: int, updated_story: StoryCreate,db: Session = Depends(get_db)):

    story = db.query(Story).filter(Story.id == id).first()

    story.title = updated_story.title
    story.content = updated_story.content
    story.author = updated_story.author

    db.commit()

    db.refresh(story)

    return story


@router.delete("/stories/{id}")
def delete_story(id: int,db: Session = Depends(get_db)):
    
        

    story = db.query(Story).filter(Story.id == id).first()

    db.delete(story)

    db.commit()

    return {"message": "Story deleted successfully"}