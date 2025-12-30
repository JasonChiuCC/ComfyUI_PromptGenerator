"""Disney animation theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class DisneyHandler(BaseThemeHandler):
    """Handler for Disney animation style prompt generation.
    
    Generates prompts inspired by classic Disney animation style,
    with magical, whimsical, and fairy tale aesthetics.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Disney style prompt components."""
        components = {}
        
        # Generate character/subject
        if custom_subject:
            character = custom_subject
        else:
            character = self._get_random_choice("disney.characters", "disney character")
        
        outfit = self._get_random_choice("disney.outfits", "magical costume")
        expression = self._get_random_choice("disney.expressions", "warm expression")
        shot_type = self._get_random_choice("disney.shot_types", "full body character shot")
        
        components["subject"] = (
            f"((Disney animation style)) {character}, "
            f"{shot_type}, wearing {outfit}, {expression}, "
            f"charming character design, classic Disney aesthetic"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("disney.locations", "magical kingdom")
            
            magic = self._get_random_choice("disney.magical_elements", "magical sparkles")
            
            components["environment"] = (
                f"in {location}, "
                f"with {magic}, "
                f"fairy tale setting, enchanted atmosphere"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            mood = self._get_random_choice("disney.moods", "magical wonder")
            
            components["style"] = (
                f"Disney animation masterpiece, "
                f"{mood}, "
                f"vibrant colors, smooth animation style, "
                f"fairy tale quality, timeless Disney magic"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            lighting = self._get_random_choice("disney.lighting", "magical light")
            
            components["effects"] = (
                f"{lighting}, "
                f"disney sparkle effects, "
                f"magical atmosphere, enchanting glow"
            )
        else:
            components["effects"] = ""
        
        return components

