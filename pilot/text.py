"""Text helpers."""


def slugify(text: str) -> str:
    """Return a lowercase, hyphen-separated slug for ``text``."""
    slug = "".join(ch if ch.isalnum() else " " for ch in text.lower())
    return "-".join(slug.split())


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in ``text``."""
    return len(text.split())
