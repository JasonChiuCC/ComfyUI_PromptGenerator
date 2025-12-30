"""Manga theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class MangaHandler(BaseThemeHandler):
    """Handler for manga style prompt generation.
    
    Generates prompts for Japanese manga illustration style,
    with characteristic black and white aesthetics, screentones, and effects.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate manga style prompt components."""
        components = {}
        
        # Generate character/subject
        if custom_subject:
            character = custom_subject
        else:
            character = self._get_random_choice("manga.characters", "manga character")
        
        genre = self._get_random_choice("manga.genres", "manga style")
        expression = self._get_random_choice("manga.expressions", "expressive face")
        pose = self._get_random_choice("manga.poses", "dynamic pose")
        shot_type = self._get_random_choice("manga.shot_types", "full body shot")
        
        components["subject"] = (
            f"((manga illustration)) of {character}, "
            f"{shot_type}, {genre} style, {expression}, {pose}, "
            f"professional manga art"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                background = custom_location
            else:
                background = self._get_random_choice("manga.backgrounds", "detailed background")
            
            components["environment"] = (
                f"in {background}, "
                f"manga background style, detailed scenery"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            panel_style = self._get_random_choice("manga.panel_styles", "manga panel")
            
            components["style"] = (
                f"professional manga art, {panel_style}, "
                f"black and white manga, screentone shading, "
                f"clean lineart, high contrast, "
                f"Japanese manga aesthetic"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            effect = self._get_random_choice("manga.effects", "manga effects")
            
            components["effects"] = (
                f"{effect}, "
                f"dramatic manga style, "
                f"professional inking, detailed hatching"
            )
        else:
            components["effects"] = ""
        
        return components

