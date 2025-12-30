"""Psychedelic art style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class PsychedelicHandler(BaseThemeHandler):
    """Handler for Psychedelic art style prompt generation.
    
    Generates prompts for psychedelic artwork with vibrant colors,
    fractal patterns, and visionary imagery.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Psychedelic prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("psychedelic.subjects", "cosmic being")
        
        composition = self._get_random_choice("psychedelic.composition_types", "kaleidoscope pattern")
        element = self._get_random_choice("psychedelic.elements", "fractal geometry")
        color_palette = self._get_random_choice("psychedelic.color_palettes", "electric rainbow")
        
        components["subject"] = (
            f"((psychedelic masterpiece)), {subject}, "
            f"{composition}, {element}, {color_palette}"
        )
        
        # Generate environment
        if include_environment:
            mood = self._get_random_choice("psychedelic.moods", "mind expansion")
            
            components["environment"] = (
                f"{mood}, cosmic consciousness, "
                f"altered perception, visionary realm"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            influence = self._get_random_choice("psychedelic.influences", "Alex Grey visionary")
            
            components["style"] = (
                f"{influence}, visionary art, "
                f"trippy artwork, 60s poster style, "
                f"consciousness expanding imagery"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"neon glow, fractal patterns, "
                f"prismatic colors, swirling forms, "
                f"bioluminescent, sacred geometry"
            )
        else:
            components["effects"] = ""
        
        return components

