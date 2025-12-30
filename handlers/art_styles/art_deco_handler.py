"""Art Deco style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class ArtDecoHandler(BaseThemeHandler):
    """Handler for Art Deco style prompt generation.
    
    Generates prompts for Art Deco with geometric patterns,
    luxurious materials, and Jazz Age glamour.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Art Deco prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("art_deco.subjects", "glamorous woman")
        
        composition = self._get_random_choice("art_deco.composition_types", "geometric symmetry")
        element = self._get_random_choice("art_deco.elements", "sunburst rays")
        color_palette = self._get_random_choice("art_deco.color_palettes", "black and gold")
        
        components["subject"] = (
            f"((Art Deco masterpiece)), {subject}, "
            f"{composition}, {element}, {color_palette}"
        )
        
        # Generate environment
        if include_environment:
            mood = self._get_random_choice("art_deco.moods", "glamorous luxury")
            
            components["environment"] = (
                f"{mood}, geometric patterns, "
                f"streamlined forms, Gatsby era elegance"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            influence = self._get_random_choice("art_deco.influences", "Chrysler Building")
            
            components["style"] = (
                f"inspired by {influence}, Jazz Age glamour, "
                f"1920s luxury aesthetic, "
                f"vintage poster quality, machine age elegance"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"chrome and gold accents, "
                f"bold geometric patterns, stepped forms, "
                f"luxurious materials, high contrast"
            )
        else:
            components["effects"] = ""
        
        return components

