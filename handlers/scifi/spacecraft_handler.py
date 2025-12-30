"""Spacecraft theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class SpacecraftHandler(BaseThemeHandler):
    """Handler for spacecraft design art."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate spacecraft prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("spacecraft.subjects", "sleek starfighter")
        
        composition = self._get_random_choice("spacecraft.composition_types", "beauty shot")
        
        components["subject"] = (
            f"((spacecraft design)) of {subject}, "
            f"{composition}, detailed spaceship art"
        )
        
        if include_environment:
            environment = self._get_random_choice("spacecraft.environments", "deep space")
            lighting = self._get_random_choice("spacecraft.lighting", "starlight on hull")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("spacecraft.styles", "hard sci-fi design")
            components["style"] = f"{style}, detailed hull, cinematic"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("spacecraft.effects", "engine trails")
            components["effects"] = f"{effect}, space environment, high detail"
        else:
            components["effects"] = ""
        
        return components





