"""Holographic 3D theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class HolographicHandler(BaseThemeHandler):
    """Handler for holographic 3D style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate holographic 3D prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("holographic.subjects", "hologram")
        
        view = self._get_random_choice("holographic.view_types", "floating display")
        
        components["subject"] = (
            f"((holographic 3D)) {subject}, "
            f"{view}, futuristic projection"
        )
        
        if include_environment:
            scene = self._get_random_choice("holographic.scenes", "dark room")
            components["environment"] = f"in {scene}, hologram display"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("holographic.styles", "sci-fi hologram")
            components["style"] = f"{style}, iridescent material, Star Wars hologram"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "chromatic aberration, scan lines, transparency, glow effect"
        else:
            components["effects"] = ""
        
        return components
