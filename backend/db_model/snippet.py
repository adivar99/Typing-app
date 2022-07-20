from sqlalchemy import Column, Integer, String, Enum
from backend.db.db import Base
from backend.models.enums import Language

class Snippet(Base):
    __tablename__ = "snippets"
    
    id = Column(Integer, primary_key=True, index=True)
    snippet = Column(String, nullable=False)
    language = Column(Enum(Language, native_enum=False, create_constraint=False), index=True)
    repo_file_name = Column(String)
    github_repo_url = Column(String)
    license = Column(String)
    commit_hash = Column(String)
    starting_line_number = Column(Integer)
    chunk_size = Column(Integer)
