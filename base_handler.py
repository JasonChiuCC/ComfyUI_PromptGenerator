"""Base handler for theme-specific prompt generation."""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
import random


# =============================================================================
# Config key mappings for different theme types
# =============================================================================

# Standard keys that handlers look for in configs
STANDARD_KEYS = {
    "subject": ["subjects", "characters", "entities", "creatures", "scenes"],
    "shot": ["shot_types", "view_types", "composition_types", "angles", "perspectives"],
    "environment": ["environments", "locations", "settings", "backgrounds", "scenes"],
    "lighting": ["lighting", "light_types", "atmospheres", "weather", "times"],
    "style": ["styles", "aesthetics", "techniques", "art_styles"],
    "mood": ["moods", "tones", "feelings", "atmospheres"],
    "effect": ["effects", "visual_effects", "special_effects", "post_effects"],
    "color": ["colors", "color_palette", "palettes", "color_schemes"],
    "detail": ["details", "elements", "features", "props", "accessories"],
}


class BaseThemeHandler(ABC):
    """Abstract base class for all theme handlers.
    
    Each theme handler defines how to combine elements from its config
    into a coherent prompt. Subclasses must implement the generate() method.
    """
    
    def __init__(self, config_manager):
        """Initialize the theme handler with a configuration manager.
        
        Args:
            config_manager: ConfigManager instance for accessing theme configs
        """
        self.config = config_manager
        self.debug_mode = False
    
    def set_debug(self, debug: bool):
        """Enable or disable debug mode.
        
        Args:
            debug: Whether to enable debug output
        """
        self.debug_mode = debug
    
    def debug_print(self, message: str):
        """Print debug message if debug mode is enabled.
        
        Args:
            message: Debug message to print
        """
        if self.debug_mode:
            print(f"[DEBUG] {self.__class__.__name__} - {message}")
    
    def _get_random_choice(self, config_key: str, default: str = "default") -> str:
        """Get a random choice from a configuration list.
        
        Args:
            config_key: Dot-notation key to access config (e.g., 'realistic.cameras')
            default: Default value if config key not found
            
        Returns:
            A randomly selected item from the config list
        """
        try:
            choices = self.config.get_config(config_key)
            if not choices:
                self._log_config_issue(f"Empty config for {config_key}", default)
                return default
            
            result = self.config.random.choice(choices)
            self.debug_print(f"Selected {config_key}: {result} (from {len(choices)} options)")
            return result
        except KeyError:
            self._log_config_issue(f"Config key not found: {config_key}", default)
            return default
        except Exception as e:
            self._log_config_issue(f"Error for {config_key}: {e}", default)
            return default
    
    def _log_config_issue(self, message: str, default: str):
        """Log a config issue. Always prints on first occurrence per key."""
        if not hasattr(self, '_logged_issues'):
            self._logged_issues = set()
        
        if message not in self._logged_issues:
            self._logged_issues.add(message)
            # Always print config issues (not just in debug mode) - helps catch bugs
            print(f"[CONFIG WARNING] {self.__class__.__name__}: {message} (using: {default})")
    
    def _get_random_choices(self, config_key: str, count: int = 1, default: str = "default") -> List[str]:
        """Get multiple random choices from a configuration list.
        
        Args:
            config_key: Dot-notation key to access config
            count: Number of items to select
            default: Default value if config key not found
            
        Returns:
            List of randomly selected items
        """
        try:
            choices = self.config.get_config(config_key)
            if not choices:
                return [default] * count
            
            # If we need more items than available, allow duplicates
            if len(choices) < count:
                return [self.config.random.choice(choices) for _ in range(count)]
            
            return self.config.random.sample(choices, count)
        except Exception as e:
            self.debug_print(f"Error getting random choices for {config_key}: {e}")
            return [default] * count
    
    @abstractmethod
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate theme-specific prompt components.
        
        This method must be implemented by each theme handler to define
        how elements are combined into a prompt.
        
        Args:
            custom_subject: Optional custom subject to override random selection
            custom_location: Optional custom location to override random selection
            include_environment: Whether to include environment in output
            include_style: Whether to include style in output
            include_effects: Whether to include effects in output
            
        Returns:
            Dictionary with keys: 'subject', 'environment', 'style', 'effects'
            Each value is a string that will be combined into the final prompt.
        """
        pass


# =============================================================================
# GenericThemeHandler - Auto-generates prompts from config structure
# =============================================================================

class GenericThemeHandler(BaseThemeHandler):
    """Generic handler that auto-generates prompts based on config structure.
    
    This handler automatically discovers available keys in a theme's config
    and uses them to build prompts. No need to write individual handler classes!
    
    Usage:
        handler = GenericThemeHandler(config_manager, "brutalist")
        components = handler.generate()
    """
    
    def __init__(self, config_manager, theme_name: str):
        """Initialize with theme name.
        
        Args:
            config_manager: ConfigManager instance
            theme_name: The theme's internal name (e.g., 'brutalist', 'anime')
        """
        super().__init__(config_manager)
        self.theme_name = theme_name
        self._available_keys = self._discover_keys()
    
    def _discover_keys(self) -> Dict[str, str]:
        """Discover what keys are available in this theme's config.
        
        Returns:
            Dict mapping standard key types to actual config keys
        """
        available = {}
        
        try:
            theme_config = self.config.get_config(self.theme_name)
            if not isinstance(theme_config, dict):
                return available
            
            config_keys = set(theme_config.keys())
            
            # Map standard types to actual keys found in config
            for std_type, possible_keys in STANDARD_KEYS.items():
                for key in possible_keys:
                    if key in config_keys:
                        available[std_type] = key
                        break
            
            # Store all available keys for reference
            self._all_config_keys = config_keys
            
        except Exception:
            self._all_config_keys = set()
        
        return available
    
    def _get_key(self, std_type: str) -> Optional[str]:
        """Get the actual config key for a standard type."""
        return self._available_keys.get(std_type)
    
    def _get_theme_value(self, std_type: str, default: str = "") -> str:
        """Get a random value for a standard type."""
        key = self._get_key(std_type)
        if key:
            return self._get_random_choice(f"{self.theme_name}.{key}", default)
        return default
    
    def _format_theme_name(self) -> str:
        """Format theme name for prompt (e.g., 'epic_fantasy' -> 'epic fantasy')."""
        return self.theme_name.replace("_", " ")
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate prompt components using discovered config keys.
        
        Automatically builds prompts based on what's available in the config.
        """
        components = {}
        theme_display = self._format_theme_name()
        
        # === SUBJECT ===
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_theme_value("subject", f"{theme_display} scene")
        
        shot = self._get_theme_value("shot", "detailed shot")
        detail = self._get_theme_value("detail", "")
        
        subject_parts = [f"(({theme_display} style))", f"of {subject}", shot]
        if detail:
            subject_parts.append(detail)
        subject_parts.append("professional quality")
        
        components["subject"] = ", ".join(filter(None, subject_parts))
        
        # === ENVIRONMENT ===
        if include_environment:
            if custom_location:
                env = custom_location
            else:
                env = self._get_theme_value("environment", "")
            
            lighting = self._get_theme_value("lighting", "")
            
            env_parts = []
            if env:
                env_parts.append(f"in {env}")
            if lighting:
                env_parts.append(lighting)
            
            components["environment"] = ", ".join(env_parts) if env_parts else ""
        else:
            components["environment"] = ""
        
        # === STYLE ===
        if include_style:
            style = self._get_theme_value("style", f"{theme_display} aesthetic")
            mood = self._get_theme_value("mood", "")
            color = self._get_theme_value("color", "")
            
            style_parts = [style]
            if mood:
                style_parts.append(mood)
            if color:
                style_parts.append(color)
            style_parts.append("highly detailed")
            
            components["style"] = ", ".join(filter(None, style_parts))
        else:
            components["style"] = ""
        
        # === EFFECTS ===
        if include_effects:
            effect = self._get_theme_value("effect", "")
            
            if effect:
                components["effects"] = f"{effect}, masterpiece quality"
            else:
                components["effects"] = "masterpiece quality, best quality"
        else:
            components["effects"] = ""
        
        return components


# =============================================================================
# Handler Factory - Creates handlers automatically from configs
# =============================================================================

def create_handler_for_theme(config_manager, theme_name: str) -> BaseThemeHandler:
    """Factory function to create a handler for any theme.
    
    Args:
        config_manager: ConfigManager instance
        theme_name: Theme's internal name
        
    Returns:
        A GenericThemeHandler instance for the theme
    """
    return GenericThemeHandler(config_manager, theme_name)


def auto_discover_handlers(config_manager) -> Dict[str, BaseThemeHandler]:
    """Automatically discover and create handlers for all themes in configs.
    
    Args:
        config_manager: ConfigManager instance with loaded configs
        
    Returns:
        Dict mapping theme_name to handler instance
    """
    handlers = {}
    
    for theme_name in config_manager.get_available_themes():
        try:
            handlers[theme_name] = GenericThemeHandler(config_manager, theme_name)
        except Exception as e:
            print(f"[WARNING] Failed to create handler for {theme_name}: {e}")
    
    return handlers

