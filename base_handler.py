"""Base handler for theme-specific prompt generation."""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional
import random


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
                self.debug_print(f"Empty config for {config_key}, using default: {default}")
                return default
            
            result = self.config.random.choice(choices)
            self.debug_print(f"Selected {config_key}: {result} (from {len(choices)} options)")
            return result
        except KeyError:
            self.debug_print(f"Config key not found: {config_key}, using default: {default}")
            return default
        except Exception as e:
            self.debug_print(f"Error getting random choice for {config_key}: {e}")
            return default
    
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

