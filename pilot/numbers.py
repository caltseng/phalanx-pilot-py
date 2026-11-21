"""Number helpers."""

from collections.abc import Iterable


def clamp(value: float, low: float, high: float) -> float:
    """Limit ``value`` to the inclusive range ``low``..``high``."""
    if low > high:
        raise ValueError("low must not be greater than high")
    return max(low, min(value, high))


def mean(values: Iterable[float]) -> float:
    """Return the arithmetic mean of ``values``."""
    items = list(values)
    if not items:
        raise ValueError("mean requires at least one value")
    return sum(items) / len(items)
