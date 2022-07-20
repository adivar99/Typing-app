from sqlite3 import IntegrityError
from typing import Optional, List
from sqlalchemy.orm import Session

from backend.db_model.snippet import Snippet as dbmodel
from backend.models.enums import Language
from backend.models.snippet import Snippet as model, SnippetCreate
from backend.db.db import db_session

def get(db_session: Session, *, id: int) -> Optional[model]:
    return (
        db_session.query(dbmodel)
        .filter(dbmodel.id == id)
        .first()
    )

def get_all(db_session: Session) -> List[model]:
    return (
        db_session.query(dbmodel)
        .limit(10)
        .all()
    )

def get_by_language(db_session: Session, * , language: Language) -> Optional[model]:
    return (
        db_session.query(dbmodel)
        .filter(dbmodel.language == language)
        .all()
    )

def create(db_session: Session, *, snippet_in: SnippetCreate) -> Optional[model]:
    snippet = dbmodel(**snippet_in.dict(exclude_unset=True))

    db_session.add(snippet)
    try:
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        raise e
    db_session.refresh()
    return snippet

def update(
    db_session: Session, *,
    snippet_in: SnippetCreate,
    snippet: dbmodel) -> Optional[model]:

    snippet_data = snippet.__dict__
    update_data = snippet_in.dict(exclude_unset=True)

    for field in update_data:
        if field in snippet_data:
            setattr(snippet, field, update_data[field])
    
    db_session.add()

    try:
        db_session.commit()
    except IntegrityError as e:
        raise e
    db_session.refresh()
    return snippet

def delete(db_session: Session, *, id: int) -> Optional[model]:
    snippet = get(db_session=db_session, id=id)
    db_session.delete(snippet)
    db_session.commit()
    return snippet



