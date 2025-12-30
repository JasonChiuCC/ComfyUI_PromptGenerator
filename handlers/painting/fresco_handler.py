"""Fresco style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class FrescoHandler(BaseThemeHandler):
    """Handler for fresco painting style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate fresco painting prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("fresco.subjects", "religious narrative")
        
        composition = self._get_random_choice("fresco.composition_types", "ceiling masterpiece")
        technique = self._get_random_choice("fresco.techniques", "buon fresco")
        location = self._get_random_choice("fresco.locations", "chapel ceiling")
        
        components["subject"] = (
            f"((fresco painting)), {subject}, "
            f"{composition}, {technique}, on {location}"
        )
        
        if include_environment:
            period = self._get_random_choice("fresco.periods", "High Renaissance")
            mood = self._get_random_choice("fresco.moods", "divine grandeur")
            
            components["environment"] = (
                f"{period} style, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"Italian fresco tradition, mural painting, "
                f"Sistine Chapel quality, monumental art"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"plaster texture, aged patina, "
                f"architectural integration, sacred atmosphere"
            )
        else:
            components["effects"] = ""
        
        return components






