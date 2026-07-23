"""
Custom filters to be used in templates.
"""

import markdown


def md2html(s: str) -> str:
    """Converts Markdown text into HTML."""
    return markdown.markdown(s, extensions=["extra"])
