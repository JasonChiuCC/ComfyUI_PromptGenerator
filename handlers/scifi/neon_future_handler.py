"""Neon Future theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class NeonFutureHandler(BaseThemeHandler):
    """Handler for neon future aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate neon future prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("neon_future.subjects", "neon-lit figure")
        
        composition = self._get_random_choice("neon_future.composition_types", "portrait with neon")
        
        components["subject"] = (
            f"((neon future art)) of {subject}, "
            f"{composition}, vibrant neon aesthetic"
        )
        
        if include_environment:
            environment = self._get_random_choice("neon_future.environments", "neon street")
            lighting = self._get_random_choice("neon_future.lighting", "vibrant neon pink")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("neon_future.styles", "synthwave aesthetic")
            components["style"] = f"{style}, outrun vibes, retrowave"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("neon_future.effects", "neon reflections")
            components["effects"] = f"{effect}, light trails, chromatic aberration"
        else:
            components["effects"] = ""
        
        return components






