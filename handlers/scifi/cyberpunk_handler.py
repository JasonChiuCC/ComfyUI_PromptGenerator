"""Cyberpunk theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class CyberpunkHandler(BaseThemeHandler):
    """Handler for cyberpunk aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate cyberpunk prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("cyberpunk.subjects", "cyberpunk character")
        
        composition = self._get_random_choice("cyberpunk.composition_types", "street level")
        
        components["subject"] = (
            f"((cyberpunk art)) of {subject}, "
            f"{composition}, high-tech low-life aesthetic"
        )
        
        if include_environment:
            environment = self._get_random_choice("cyberpunk.environments", "neon city")
            lighting = self._get_random_choice("cyberpunk.lighting", "neon glow")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("cyberpunk.styles", "cyberpunk")
            components["style"] = f"{style}, Blade Runner inspired, detailed"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("cyberpunk.effects", "neon reflections")
            components["effects"] = f"{effect}, dystopian future, high quality"
        else:
            components["effects"] = ""
        
        return components





