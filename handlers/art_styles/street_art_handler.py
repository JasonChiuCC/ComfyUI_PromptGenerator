"""Street Art style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class StreetArtHandler(BaseThemeHandler):
    """Handler for Street Art style prompt generation.
    
    Generates prompts for street art with murals, stencils,
    and public intervention aesthetics.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Street Art prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("street_art.subjects", "social commentary")
        
        composition = self._get_random_choice("street_art.composition_types", "building facade mural")
        style = self._get_random_choice("street_art.styles", "stencil art")
        element = self._get_random_choice("street_art.elements", "spray paint texture")
        
        components["subject"] = (
            f"((street art masterpiece)), {subject}, "
            f"{composition}, {style}, {element}"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                mood = self._get_random_choice("street_art.moods", "urban rebellion")
            
            components["environment"] = (
                f"{mood}, urban context, "
                f"public space, city environment"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            influence = self._get_random_choice("street_art.influences", "Banksy subversion")
            
            components["style"] = (
                f"{influence} inspired, contemporary muralism, "
                f"public art movement, "
                f"urban art gallery quality"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"wall texture, site-specific, "
                f"weathered surface, authentic urban feel, "
                f"spray paint finish"
            )
        else:
            components["effects"] = ""
        
        return components

