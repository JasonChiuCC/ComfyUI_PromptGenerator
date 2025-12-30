"""
ComfyUI Prompt Generator - Custom Node Package

A theme-based prompt generator that uses random element combinations
to create diverse and creative prompts for image generation.

Features:
- Category-separated nodes (Animation, Art Style, etc.)
- Multiple theme support per category
- Random element combination from JSON configs
- Hot reload for development (JSON + Python)
- Seed-based reproducibility
- English and Chinese UI support
"""

__version__ = "2.0.0"
__author__ = "JC"

# Import node classes
from .prompt_generator import (
    NODE_CLASS_MAPPINGS,
    NODE_DISPLAY_NAME_MAPPINGS,
)

# Export for ComfyUI
__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
]
