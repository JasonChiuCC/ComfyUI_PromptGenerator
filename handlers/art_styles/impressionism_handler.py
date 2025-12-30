"""Impressionism art style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class ImpressionismHandler(BaseThemeHandler):
    """Handler for Impressionism art style prompt generation.
    
    Generates prompts for Impressionist artwork with light effects,
    visible brushstrokes, and fleeting moments.
    """
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Impressionism prompt components."""
        components = {}
        
        # Generate subject
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("impressionism.subjects", "sunlit garden")
        
        composition = self._get_random_choice("impressionism.composition_types", "en plein air")
        element = self._get_random_choice("impressionism.elements", "dappled sunlight")
        technique = self._get_random_choice("impressionism.techniques", "broken color")
        
        components["subject"] = (
            f"((Impressionist masterpiece)), {subject}, "
            f"{composition}, {element}, {technique}"
        )
        
        # Generate environment
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                mood = self._get_random_choice("impressionism.moods", "joyful luminosity")
            
            components["environment"] = (
                f"{mood}, natural light, "
                f"atmospheric haze, outdoor setting"
            )
        else:
            components["environment"] = ""
        
        # Generate style
        if include_style:
            influence = self._get_random_choice("impressionism.influences", "Monet style")
            
            components["style"] = (
                f"{influence}, museum quality, "
                f"French Impressionism, plein air painting, "
                f"19th century masterpiece"
            )
        else:
            components["style"] = ""
        
        # Generate effects
        if include_effects:
            components["effects"] = (
                f"visible brushstrokes, light effects, "
                f"color vibration, optical mixing, "
                f"soft edges, luminous atmosphere"
            )
        else:
            components["effects"] = ""
        
        return components

