"""Anime theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class AnimeHandler(BaseThemeHandler):
    """Handler for anime style prompt generation.
    
    Generates prompts for Japanese animation style artwork,
    including characters, expressions, and anime-specific effects.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate anime style prompt components.
        
        Args:
            custom_subject: Optional custom character override
            custom_location: Optional custom location override
            include_environment: Whether to include background/setting
            include_style: Whether to include anime style details
            include_effects: Whether to include visual effects
            
        Returns:
            Dictionary with prompt components
        """
        components = {}
        
        # Generate character/subject
        if custom_subject:
            character = custom_subject
        else:
            character = self._get_random_choice("anime.characters", "anime character")
        
        outfit = self._get_random_choice("anime.outfits", "stylish outfit")
        expression = self._get_random_choice("anime.expressions", "expressive face")
        pose = self._get_random_choice("anime.poses", "dynamic pose")
        shot_type = self._get_random_choice("anime.shot_types", "full body shot")
        
        components["subject"] = (
            f"((masterpiece anime art)) of {character}, "
            f"{shot_type}, wearing {outfit}, {expression}, {pose}, "
            f"professional anime illustration"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("anime.locations", "anime background")
            
            time = self._get_random_choice("anime.times", "dramatic lighting")
            weather = self._get_random_choice("anime.weather", "atmospheric effects")
            
            components["environment"] = (
                f"in {location}, during {time}, "
                f"{weather}, detailed anime background"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            style = self._get_random_choice("anime.styles", "anime style")
            studio = self._get_random_choice("anime.studios", "professional studio")
            
            components["style"] = (
                f"{style}, inspired by {studio} quality, "
                f"vibrant colors, clean line art, "
                f"professional cel shading, 8k resolution"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            effect = self._get_random_choice("anime.effects", "visual effects")
            lighting = self._get_random_choice("anime.lighting", "dramatic lighting")
            
            components["effects"] = (
                f"{effect}, {lighting}, "
                f"volumetric lighting, anime visual excellence"
            )
        else:
            components["effects"] = ""
        
        return components

