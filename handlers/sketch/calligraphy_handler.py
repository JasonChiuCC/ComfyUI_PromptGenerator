"""Calligraphy style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class CalligraphyHandler(BaseThemeHandler):
    """Handler for calligraphy style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate calligraphy prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("calligraphy.subjects", "elegant lettering")
        
        composition = self._get_random_choice("calligraphy.composition_types", "flowing script")
        style = self._get_random_choice("calligraphy.styles", "Western calligraphy")
        technique = self._get_random_choice("calligraphy.techniques", "thick thin variation")
        
        components["subject"] = (
            f"((calligraphy art)), {subject}, "
            f"{composition}, {style}, {technique}"
        )
        
        if include_environment:
            tool = self._get_random_choice("calligraphy.tools", "pointed nib")
            mood = self._get_random_choice("calligraphy.moods", "elegant refinement")
            
            components["environment"] = (
                f"created with {tool}, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"traditional calligraphy, hand lettering, "
                f"artistic script, professional typography"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"flowing strokes, elegant curves, "
                f"ink variation, masterful control"
            )
        else:
            components["effects"] = ""
        
        return components






