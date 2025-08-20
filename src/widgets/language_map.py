# Mapping of common programming languages to their file extensions
LANGUAGE_EXTENSIONS = {
    "python": [".py"],
    "javascript": [".js"],
    "typescript": [".ts"],
    "java": [".java"],
    "c": [".c"],
    "cpp": [".cpp", ".cc", ".cxx", ".hpp", ".h"],
    "csharp": [".cs"],
    "go": [".go"],
    "ruby": [".rb"],
    "php": [".php"],
    "swift": [".swift"],
    "kotlin": [".kt", ".kts"],
    "rust": [".rs"],
    "scala": [".scala"],
    "perl": [".pl", ".pm"],
    "html": [".html", ".htm"],
    "css": [".css", ".tcss"],
    "json": [".json"],
    "yaml": [".yaml", ".yml"],
    "xml": [".xml"],
    "shell": [".sh", ".bash"],
    "makefile": ["Makefile"],
    "markdown": [".md"],
    "dart": [".dart"],
    "r": [".r"],
    "lua": [".lua"],
    "objective-c": [".m", ".mm"],
    "powershell": [".ps1"],
    "sql": [".sql"],
}

def get_language_from_extension(suffix):
    for language, extensions in LANGUAGE_EXTENSIONS.items():
        if suffix in extensions:
            return language
    return None
