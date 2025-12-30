"""Crayon style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class CrayonHandler(BaseThemeHandler):
    """Handler for crayon art style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate crayon art prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("crayon.subjects", "happy family")
        
        composition = self._get_random_choice("crayon.composition_types", "childlike drawing")
        technique = self._get_random_choice("crayon.techniques", "bold strokes")
        crayon_type = self._get_random_choice("crayon.crayon_types", "wax crayons")
        
        components["subject"] = (
            f"((crayon drawing)), {subject}, "
            f"{composition}, {technique}, using {crayon_type}"
        )
        
        if include_environment:
            quality = self._get_random_choice("crayon.qualities", "waxy texture")
            mood = self._get_random_choice("crayon.moods", "innocent joy")
            
            components["environment"] = (
                f"{quality}, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"childlike art style, naive charm, "
                f"playful drawing, nostalgic quality"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"bold colors, visible strokes, "
                f"simple shapes, waxy finish"
            )
        else:
            components["effects"] = ""
        
        return components






