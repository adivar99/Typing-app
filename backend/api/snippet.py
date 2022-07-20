import random
from fastapi import Depends
from sqlalchemy.orm import Session

from backend.db.db import db_session
from backend.crud.snippet import create, delete, get, get_all, get_by_language, update
from backend.models.enums import Language
from backend.models.snippet import Snippet, SnippetCreate

def get_snippet(id: int, db_session: Session = db_session):
    return get(db_session, id=id)

def get_all_snippets(db_session: Session = db_session):
    return get_all(db_session)

def get_random_snippet(db_session: Session = db_session):
    snippet_ids = [snip.id for snip in get_by_language(db_session, language=Language.PYTHON)]    
    return get(db_session, id=random.choice(snippet_ids)).snippet

def create_snippet(snippet_in: SnippetCreate, db_session: Session = db_session):
    return create(db_session, snippet_in=snippet_in)

def update_snippet(snippet_in: SnippetCreate, db_session: Session = db_session):
    return update(db_session, snippet_in=snippet_in)

def delete_snippet(id: int, db_session: Session = db_session):
    return delete(db_session, id=id)