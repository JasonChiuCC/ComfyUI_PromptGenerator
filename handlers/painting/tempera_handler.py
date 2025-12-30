"""Tempera style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class TemperaHandler(BaseThemeHandler):
    """Handler for tempera painting style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate tempera painting prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("tempera.subjects", "sacred figure")
        
        composition = self._get_random_choice("tempera.composition_types", "religious icon")
        technique = self._get_random_choice("tempera.techniques", "egg yolk binder")
        characteristic = self._get_random_choice("tempera.characteristics", "luminous color")
        
        components["subject"] = (
            f"((tempera painting)), {subject}, "
            f"{composition}, {technique}, {characteristic}"
        )
        
        if include_environment:
            tradition = self._get_random_choice("tempera.traditions", "Byzantine icon")
            mood = self._get_random_choice("tempera.moods", "sacred devotion")
            
            components["environment"] = (
                f"{tradition} style, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"egg tempera tradition, icon painting, "
                f"medieval technique, sacred art quality"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"gold leaf gilding, matte finish, "
                f"jewel-like colors, luminous glow"
            )
        else:
            components["effects"] = ""
        
        return components






