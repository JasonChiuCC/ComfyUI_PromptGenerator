"""Elven theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class ElvenHandler(BaseThemeHandler):
    """Handler for elven aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate elven prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("elven.subjects", "elven queen")
        
        shot_type = self._get_random_choice("elven.shot_types", "elegant portrait")
        
        components["subject"] = (
            f"((elven fantasy art)) of {subject}, "
            f"{shot_type}, ethereal elven beauty"
        )
        
        if include_environment:
            environment = self._get_random_choice("elven.environments", "elven tree city")
            lighting = self._get_random_choice("elven.lighting", "ethereal moonlight")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("elven.styles", "elven fantasy")
            components["style"] = f"{style}, graceful elegance, Tolkien inspired"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("elven.effects", "leaf and nature magic")
            components["effects"] = f"{effect}, ethereal glow, timeless beauty"
        else:
            components["effects"] = ""
        
        return components






