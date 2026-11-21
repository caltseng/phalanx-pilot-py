"""Text helpers."""


def slugify(text: str) -> str:
    """Return a lowercase, hyphen-separated slug for ``text``."""
    slug = "".join(ch if ch.isalnum() else "-" for ch in text.lower())
    return slug.strip("-")


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in ``text``."""
    return len(text.split())


ELLIPSIS = "\u2026"


def truncate(text: str, width: int) -> str:
    """Return ``text`` shortened to at most ``width`` characters.

    Longer text keeps its first ``width - 1`` characters followed by a single
    horizontal ellipsis (U+2026). ``width`` must be at least 1.
    """
    if width < 1:
        raise ValueError("width must be at least 1")
    if len(text) <= width:
        return text
    return text[: width - 1] + ELLIPSIS
