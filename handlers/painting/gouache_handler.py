"""Gouache style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class GouacheHandler(BaseThemeHandler):
    """Handler for gouache painting style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate gouache painting prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("gouache.subjects", "illustrated scene")
        
        composition = self._get_random_choice("gouache.composition_types", "illustration style")
        technique = self._get_random_choice("gouache.techniques", "flat application")
        quality = self._get_random_choice("gouache.qualities", "matte finish")
        
        components["subject"] = (
            f"((gouache painting)), {subject}, "
            f"{composition}, {technique}, {quality}"
        )
        
        if include_environment:
            style = self._get_random_choice("gouache.styles", "mid-century modern")
            mood = self._get_random_choice("gouache.moods", "illustrative charm")
            
            components["environment"] = (
                f"{style}, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"traditional gouache, opaque watercolor, "
                f"illustration quality, professional finish"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"velvety matte surface, opaque coverage, "
                f"crisp edges, rich pigment"
            )
        else:
            components["effects"] = ""
        
        return components






