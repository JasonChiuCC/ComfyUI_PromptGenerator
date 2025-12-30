"""Glitch Art style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class GlitchArtHandler(BaseThemeHandler):
    """Handler for Glitch Art style prompt generation.
    
    Generates prompts for glitch artwork with digital corruption,
    pixel displacement, and data aesthetics.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Glitch Art prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("glitch_art.subjects", "distorted portrait")
        
        composition = self._get_random_choice("glitch_art.composition_types", "corrupted image")
        effect = self._get_random_choice("glitch_art.effects", "pixel sorting")
        color_palette = self._get_random_choice("glitch_art.color_palettes", "RGB channel split")
        
        components["subject"] = (
            f"((glitch art)), {subject}, "
            f"{composition}, {effect}, {color_palette}"
        )
        
        # Generate environment
        if include_environment:
            mood = self._get_random_choice("glitch_art.moods", "digital anxiety")
            
            components["environment"] = (
                f"{mood}, corrupted reality, "
                f"digital decay, system failure aesthetic"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            technique = self._get_random_choice("glitch_art.techniques", "databending")
            
            components["style"] = (
                f"{technique}, post-digital art, "
                f"intentional corruption, "
                f"new media art, digital avant-garde"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"scan lines, compression artifacts, "
                f"VHS distortion, RGB split, "
                f"pixel displacement, digital noise"
            )
        else:
            components["effects"] = ""
        
        return components

