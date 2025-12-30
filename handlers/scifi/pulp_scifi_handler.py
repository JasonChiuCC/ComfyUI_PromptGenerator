"""Pulp Sci-Fi theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class PulpSciFiHandler(BaseThemeHandler):
    """Handler for pulp sci-fi aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate pulp sci-fi prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("pulp_scifi.subjects", "space hero")
        
        composition = self._get_random_choice("pulp_scifi.composition_types", "magazine cover composition")
        
        components["subject"] = (
            f"((pulp sci-fi art)) of {subject}, "
            f"{composition}, classic magazine cover style"
        )
        
        if include_environment:
            environment = self._get_random_choice("pulp_scifi.environments", "alien planet surface")
            lighting = self._get_random_choice("pulp_scifi.lighting", "dramatic pulp lighting")
            components["environment"] = f"on {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("pulp_scifi.styles", "Amazing Stories style")
            components["style"] = f"{style}, Golden Age sci-fi, retro adventure"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("pulp_scifi.effects", "ray gun beams")
            components["effects"] = f"{effect}, rocket exhaust, dramatic action"
        else:
            components["effects"] = ""
        
        return components





