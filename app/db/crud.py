import random
import string

from sqlalchemy.orm import Session

from app.models.url import URL


def generate_short_code(db: Session, length=6):
    while True:
        short_code = "".join(
            random.choices(string.ascii_letters + string.digits, k=length)
        )
        if not db.query(URL).filter(URL.short_code == short_code).first():
            return short_code


def create_short_url(db: Session, original_url: str) -> URL:
    short_code = generate_short_code(db)
    new_url = URL(original_url=original_url, short_code=short_code)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return new_url


def get_url_by_code(db: Session, code: str) -> URL:
    return db.query(URL).filter(URL.short_code == code).first()
