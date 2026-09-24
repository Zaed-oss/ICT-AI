"""
Strategy package.

The legacy built-in trading strategies have been removed.
This package now provides the strategy contract and shared
analysis infrastructure used by the AI trading platform.
"""

from .base import BaseStrategy

__all__ = [
    "BaseStrategy",
]
