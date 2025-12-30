"""Webtoon (Korean webcomic) theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class WebtoonHandler(BaseThemeHandler):
    """Handler for Korean webtoon style prompt generation.
    
    Generates prompts for Korean webcomic style, characterized by
    clean digital art, vibrant colors, and modern aesthetics.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate webtoon style prompt components."""
        components = {}
        
        # Generate character/subject
        if custom_subject:
            character = custom_subject
        else:
            character = self._get_random_choice("webtoon.characters", "webtoon character")
        
        genre = self._get_random_choice("webtoon.genres", "webtoon story")
        expression = self._get_random_choice("webtoon.expressions", "expressive face")
        shot_type = self._get_random_choice("webtoon.shot_types", "full body shot")
        
        components["subject"] = (
            f"((Korean webtoon style)) {character}, "
            f"{shot_type}, {genre}, {expression}, "
            f"manhwa illustration"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                background = custom_location
            else:
                background = self._get_random_choice("webtoon.backgrounds", "modern setting")
            
            components["environment"] = (
                f"in {background}, "
                f"detailed webtoon background"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            art_style = self._get_random_choice("webtoon.art_styles", "webtoon art")
            
            components["style"] = (
                f"{art_style}, "
                f"Korean manhwa style, "
                f"clean digital illustration, "
                f"professional webtoon quality, vertical scroll format"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            effect = self._get_random_choice("webtoon.effects", "visual effects")
            lighting = self._get_random_choice("webtoon.lighting", "soft lighting")
            
            components["effects"] = (
                f"{effect}, {lighting}, "
                f"polished finish, vibrant colors"
            )
        else:
            components["effects"] = ""
        
        return components

