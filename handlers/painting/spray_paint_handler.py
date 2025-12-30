"""Spray Paint style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class SprayPaintHandler(BaseThemeHandler):
    """Handler for spray paint art style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate spray paint art prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("spray_paint.subjects", "cosmic galaxy")
        
        composition = self._get_random_choice("spray_paint.composition_types", "space scene")
        technique = self._get_random_choice("spray_paint.techniques", "layered spraying")
        style = self._get_random_choice("spray_paint.styles", "space art")
        
        components["subject"] = (
            f"((spray paint art)), {subject}, "
            f"{composition}, {technique}, {style}"
        )
        
        if include_environment:
            tool = self._get_random_choice("spray_paint.tools", "various caps")
            mood = self._get_random_choice("spray_paint.moods", "cosmic wonder")
            
            components["environment"] = (
                f"created with {tool}, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"aerosol art, street performance style, "
                f"speed painting, cosmic landscapes"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"smooth gradients, planet textures, "
                f"star splatter, nebula effects"
            )
        else:
            components["effects"] = ""
        
        return components





