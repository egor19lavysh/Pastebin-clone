from enum import Enum


class PasteVisibility(str, Enum):
    """Enum для определения уровня видимости пасты."""

    PUBLIC = "public"
    UNLISTED = "unlisted"
    PRIVATE = "private"


class SyntaxType(str, Enum):
    """
    Enum для поддерживаемых языков программирования и форматов.
    """
    # Основные языки программирования
    PLAINTEXT = "plaintext"
    PYTHON = "python"
    JAVASCRIPT = "javascript"
    TYPESCRIPT = "typescript"
    JAVA = "java"
    CPP = "cpp"  # C++
    C = "c"
    CSHARP = "csharp"  # C#
    GO = "go"
    RUST = "rust"
    PHP = "php"
    RUBY = "ruby"
    SWIFT = "swift"
    KOTLIN = "kotlin"
    
    # Веб-технологии
    HTML = "html"
    CSS = "css"
    XML = "xml"
    JSON = "json"
    YAML = "yaml"
    MARKDOWN = "markdown"
    SQL = "sql"

class ExpireAt(str, Enum):
    """
    Enum для определения времени хранения пасты.
    """

    TEN_MIN = "10m"
    ONE_HOUR = "1h"
    TEN_HOUR = "10h"
    ONE_DAY = "1d"
    SEVEN_DAYS = "7d"
    NEVER = "never"