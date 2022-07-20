import enum

class Language(enum.Enum):
    BASH = "Bash"
    C = "C"
    C_PLUS = "C++"
    CSV = "CSV"
    DOTFILE = "DOTFILE"
    GO = "Go"
    HTML = "HTML"
    JSON = "JSON"
    JAVA = "Java"
    JavaScript = "JavaScript"
    JUPYTER = "Jupyter"
    MARKDOWN = "Markdown"
    POWERSHELL = "Powershell"
    PYTHON = "Python"
    RUBY = "Ruby"
    RUST = "Rust"
    SHELL = "Shell"
    TSV = "TSV"
    TEXT = "Text"
    UNKNOWN = "UNKNOWN"
    YAML = "YAML"

class Mode(enum.Enum):
    CODE = "code"
    TEXT = "text"