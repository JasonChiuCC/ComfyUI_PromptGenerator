"""Acrylic style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class AcrylicHandler(BaseThemeHandler):
    """Handler for acrylic painting style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate acrylic painting prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("acrylic.subjects", "modern portrait")
        
        composition = self._get_random_choice("acrylic.composition_types", "contemporary style")
        technique = self._get_random_choice("acrylic.techniques", "thick impasto")
        finish = self._get_random_choice("acrylic.finishes", "matte finish")
        
        components["subject"] = (
            f"((acrylic painting)), {subject}, "
            f"{composition}, {technique}, {finish}"
        )
        
        if include_environment:
            color = self._get_random_choice("acrylic.color_qualities", "vibrant saturation")
            mood = self._get_random_choice("acrylic.moods", "contemporary energy")
            
            components["environment"] = (
                f"{color}, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"modern acrylic art, contemporary painting, "
                f"versatile medium, professional quality"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"bold colors, quick drying layers, "
                f"textured surface, vibrant finish"
            )
        else:
            components["effects"] = ""
        
        return components





