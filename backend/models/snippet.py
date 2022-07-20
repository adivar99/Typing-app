from pydantic import BaseModel, Field
from backend.models.enums import Language

class Snippet(BaseModel):
    snippet: str = Field(None, title="Code snippet", example="version = '7'\nhtml_title = \"Guzzle Documentation\"\nhtml_short_title = \"Guzzle 7\"\n\nexclude_patterns = ['_build']")
    language: Language = Field(None, title="Coding Language", example=Language.JSON)
    repo_file_name: str = Field(None, title="file name of repository", example="guzzle/guzzle/docs/conf.py")
    github_repo_url: str = Field(None, title="URL of source github repo", example="https://github.com/guzzle/guzzle")
    license: str = Field(None, title="License applied to  code snippet", example="MIT")
    commit_hash: str = Field(None, title="hash of commit in repo", example="55d46a8ba3239be2439fb660b5cc9fba69155113")
    starting_line_number: int = Field(None, title="Starting line number", example="15")
    chunk_size: int = Field(None, title="", example="5")

class SnippetCreate(Snippet):
    id: int = Field(None, title="id of snippet", example="1")
