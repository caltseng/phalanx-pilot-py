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


def median(values: Iterable[float]) -> float:
    """Return the median of ``values``.

    For an even count, return the mean of the two middle values.
    """
    items = sorted(values)
    if not items:
        raise ValueError("median requires at least one value")
    middle = len(items) // 2
    if len(items) % 2:
        return items[middle]
    return (items[middle - 1] + items[middle]) / 2
