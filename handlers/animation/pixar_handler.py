"""Pixar animation theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class PixarHandler(BaseThemeHandler):
    """Handler for Pixar 3D animation style prompt generation.
    
    Generates prompts inspired by Pixar's distinctive 3D animation style,
    with emotional depth, detailed rendering, and heartwarming aesthetics.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Pixar style prompt components."""
        components = {}
        
        # Generate character/subject
        if custom_subject:
            character = custom_subject
        else:
            character = self._get_random_choice("pixar.characters", "Pixar character")
        
        trait = self._get_random_choice("pixar.character_traits", "expressive personality")
        expression = self._get_random_choice("pixar.expressions", "heartfelt expression")
        shot_type = self._get_random_choice("pixar.shot_types", "full body character shot")
        
        components["subject"] = (
            f"((Pixar 3D animation style)) {character}, "
            f"{shot_type}, {trait}, {expression}, "
            f"detailed Pixar design, appealing character"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("pixar.locations", "colorful world")
            
            components["environment"] = (
                f"in {location}, "
                f"detailed 3D environment, "
                f"Pixar world design, rich atmosphere"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            render = self._get_random_choice("pixar.render_styles", "Pixar render")
            mood = self._get_random_choice("pixar.moods", "heartwarming")
            
            components["style"] = (
                f"{render}, {mood}, "
                f"Pixar movie quality, "
                f"cinematic 3D animation, "
                f"Disney Pixar masterpiece"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            lighting = self._get_random_choice("pixar.lighting", "Pixar lighting")
            
            components["effects"] = (
                f"{lighting}, "
                f"global illumination, "
                f"ray traced reflections, "
                f"cinema quality render"
            )
        else:
            components["effects"] = ""
        
        return components

