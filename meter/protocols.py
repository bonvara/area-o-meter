from typing import Protocol


class HasArea(Protocol):
    """Protocol for geometric objects that have an area defined."""

    def get_area(self) -> float:
        """Calculate the area of the shape."""
        ...
