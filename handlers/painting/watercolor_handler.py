"""Watercolor style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class WatercolorHandler(BaseThemeHandler):
    """Handler for watercolor style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate watercolor prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("watercolor.subjects", "flowing landscape")
        
        composition = self._get_random_choice("watercolor.composition_types", "loose landscape")
        technique = self._get_random_choice("watercolor.techniques", "wet-on-wet")
        effect = self._get_random_choice("watercolor.effects", "transparent layers")
        
        components["subject"] = (
            f"((watercolor painting)), {subject}, "
            f"{composition}, {technique}, {effect}"
        )
        
        if include_environment:
            paper = self._get_random_choice("watercolor.paper_types", "cold press texture")
            mood = self._get_random_choice("watercolor.moods", "light and airy")
            
            components["environment"] = (
                f"on {paper}, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"traditional watercolor, aquarelle painting, "
                f"fine art quality, professional illustration"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"flowing washes, luminous transparency, "
                f"soft edges, white paper glow"
            )
        else:
            components["effects"] = ""
        
        return components





