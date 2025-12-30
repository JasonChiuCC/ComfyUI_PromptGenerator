"""Graffiti art style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class GraffitiHandler(BaseThemeHandler):
    """Handler for Graffiti art style prompt generation.
    
    Generates prompts for graffiti artwork with spray paint aesthetics,
    wildstyle lettering, and urban culture.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Graffiti prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("graffiti.subjects", "wildstyle letters")
        
        composition = self._get_random_choice("graffiti.composition_types", "wall mural wide shot")
        style = self._get_random_choice("graffiti.styles", "wildstyle complex")
        element = self._get_random_choice("graffiti.elements", "spray paint drips")
        
        components["subject"] = (
            f"((graffiti masterpiece)), {subject}, "
            f"{composition}, {style}, {element}"
        )
        
        # Generate environment
        if include_environment:
            mood = self._get_random_choice("graffiti.moods", "urban energy")
            
            components["environment"] = (
                f"{mood}, urban wall, "
                f"street context, city environment"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            influence = self._get_random_choice("graffiti.influences", "New York subway")
            
            components["style"] = (
                f"{influence} style, authentic street art, "
                f"aerosol art, urban culture, "
                f"underground art movement"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"spray paint texture, bold outlines, "
                f"vibrant fills, drip effects, "
                f"3D shadows, chrome highlights"
            )
        else:
            components["effects"] = ""
        
        return components

