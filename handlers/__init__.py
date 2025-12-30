"""Theme handlers package.

This module provides handlers for all theme types.

Architecture:
1. Custom handlers (in subfolders) take priority - for themes needing special logic
2. GenericThemeHandler auto-handles any theme with a config file
3. auto_discover_all_handlers() combines both sources

This means:
- To add a new theme: just add a JSON config file, no Python needed!
- To customize a theme: write a custom handler class, it will override generic
"""

import os
import importlib
from typing import Dict, Type, Any

from ..base_handler import BaseThemeHandler, GenericThemeHandler, auto_discover_handlers


# =============================================================================
# Auto-import existing custom handlers from subfolders
# =============================================================================

def _import_category_handlers(category_name: str) -> Dict[str, Type[BaseThemeHandler]]:
    """Import handlers from a category subfolder.
    
    Args:
        category_name: Name of the subfolder (e.g., 'animation', 'horror')
        
    Returns:
        Dict mapping theme_name to handler class
    """
    handlers = {}
    
    try:
        # Import the category's __init__.py
        module = importlib.import_module(f".{category_name}", package=__name__)
        
        # Look for a HANDLERS dict (e.g., ANIMATION_HANDLERS)
        handler_dict_names = [
            f"{category_name.upper()}_HANDLERS",
            f"{category_name.upper().replace('_', '')}_HANDLERS",
            "HANDLERS",
        ]
        
        for dict_name in handler_dict_names:
            if hasattr(module, dict_name):
                category_handlers = getattr(module, dict_name)
                if isinstance(category_handlers, dict):
                    handlers.update(category_handlers)
                break
                
    except ImportError as e:
        # Category doesn't have an __init__.py or has import errors
        pass
    except Exception as e:
        pass
    
    return handlers


def _discover_categories() -> list:
    """Discover all category subfolders in handlers/."""
    handlers_dir = os.path.dirname(__file__)
    categories = []
    
    for item in os.listdir(handlers_dir):
        item_path = os.path.join(handlers_dir, item)
        if os.path.isdir(item_path) and not item.startswith('_'):
            # Check if it has an __init__.py
            if os.path.exists(os.path.join(item_path, '__init__.py')):
                categories.append(item)
    
    return categories


# =============================================================================
# Load all custom handlers from subfolders
# =============================================================================

CUSTOM_HANDLERS: Dict[str, Type[BaseThemeHandler]] = {}

# Discover and import all category handlers
_categories = _discover_categories()
for _category in _categories:
    _category_handlers = _import_category_handlers(_category)
    CUSTOM_HANDLERS.update(_category_handlers)


# =============================================================================
# Main function to get all handlers (custom + generic fallback)
# =============================================================================

def get_all_handlers(config_manager) -> Dict[str, BaseThemeHandler]:
    """Get all handlers: custom handlers + generic handlers for remaining themes.
    
    Priority:
    1. Custom handlers (from category subfolders) - for special logic
    2. GenericThemeHandler - auto-generated for any config without custom handler
    
    Args:
        config_manager: ConfigManager instance with loaded configs
        
    Returns:
        Dict mapping theme_name to handler instance
    """
    handlers = {}
    
    # First, instantiate all custom handlers
    for theme_name, handler_class in CUSTOM_HANDLERS.items():
        try:
            handlers[theme_name] = handler_class(config_manager)
        except Exception as e:
            print(f"[WARNING] Failed to init custom handler {theme_name}: {e}")
    
    # Then, create generic handlers for any theme without a custom handler
    available_themes = config_manager.get_available_themes()
    
    for theme_name in available_themes:
        if theme_name not in handlers:
            try:
                handlers[theme_name] = GenericThemeHandler(config_manager, theme_name)
            except Exception as e:
                print(f"[WARNING] Failed to create generic handler for {theme_name}: {e}")
    
    return handlers


# =============================================================================
# Legacy support: HANDLER_CLASSES dict (for backwards compatibility)
# =============================================================================

# This is used by ThemeRegistry in prompt_generator.py
# It maps theme_name to handler CLASS (not instance)
HANDLER_CLASSES = CUSTOM_HANDLERS.copy()


# =============================================================================
# Export all custom handler classes for backwards compatibility
# =============================================================================

# Import all custom handlers for direct access
try:
    from .animation import *
except ImportError:
    pass

try:
    from .art_styles import *
except ImportError:
    pass

try:
    from .sketch import *
except ImportError:
    pass

try:
    from .painting import *
except ImportError:
    pass

try:
    from .render_3d import *
except ImportError:
    pass

try:
    from .photography import *
except ImportError:
    pass

try:
    from .portrait import *
except ImportError:
    pass

try:
    from .animals import *
except ImportError:
    pass

try:
    from .scifi import *
except ImportError:
    pass

try:
    from .fantasy import *
except ImportError:
    pass

try:
    from .horror import *
except ImportError:
    pass

try:
    from .architecture import *
except ImportError:
    pass

try:
    from .nature import *
except ImportError:
    pass


__all__ = [
    'BaseThemeHandler',
    'GenericThemeHandler',
    'HANDLER_CLASSES',
    'CUSTOM_HANDLERS',
    'get_all_handlers',
]
