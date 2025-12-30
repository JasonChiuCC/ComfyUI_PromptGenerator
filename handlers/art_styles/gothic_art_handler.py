"""Gothic Art style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class GothicArtHandler(BaseThemeHandler):
    """Handler for Gothic Art style prompt generation.
    
    Generates prompts for Gothic artwork with cathedral architecture,
    stained glass, and medieval religious imagery.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Gothic Art prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("gothic_art.subjects", "religious figure")
        
        composition = self._get_random_choice("gothic_art.composition_types", "cathedral interior")
        element = self._get_random_choice("gothic_art.elements", "pointed arches")
        color_palette = self._get_random_choice("gothic_art.color_palettes", "deep ultramarine blue")
        
        components["subject"] = (
            f"((Gothic art masterpiece)), {subject}, "
            f"{composition}, {element}, {color_palette}"
        )
        
        # Generate environment
        if include_environment:
            mood = self._get_random_choice("gothic_art.moods", "spiritual devotion")
            
            components["environment"] = (
                f"{mood}, sacred space, "
                f"cathedral atmosphere, divine light"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            style = self._get_random_choice("gothic_art.styles", "high gothic")
            
            components["style"] = (
                f"{style}, medieval masterpiece, "
                f"illuminated manuscript quality, "
                f"stained glass beauty"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"gold leaf accents, rich pigments, "
                f"intricate tracery, "
                f"jewel tones, sacred symbolism"
            )
        else:
            components["effects"] = ""
        
        return components

