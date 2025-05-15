from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db import crud
from app.db.database import SessionLocal

router = APIRouter()


# Define the request body using a Pydantic model
class URLRequest(BaseModel):
    original_url: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/shorten")
def shorten_url(request: URLRequest, db: Session = Depends(get_db)):
    return crud.create_short_url(db, request.original_url)


@router.get("/{code}")
def redirect(code: str, db: Session = Depends(get_db)):
    url = crud.get_url_by_code(db, code)
    if url:
        return RedirectResponse(url.original_url)
    raise HTTPException(status_code=404, detail="URL not found")
