"""Steampunk theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class SteampunkHandler(BaseThemeHandler):
    """Handler for steampunk aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate steampunk prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("steampunk.subjects", "steampunk inventor")
        
        composition = self._get_random_choice("steampunk.composition_types", "adventure portrait")
        
        components["subject"] = (
            f"((steampunk art)) of {subject}, "
            f"{composition}, Victorian industrial aesthetic"
        )
        
        if include_environment:
            environment = self._get_random_choice("steampunk.environments", "clockwork factory")
            lighting = self._get_random_choice("steampunk.lighting", "gas lamp glow")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("steampunk.styles", "steampunk")
            components["style"] = f"{style}, brass and copper, highly detailed"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("steampunk.effects", "steam clouds")
            components["effects"] = f"{effect}, clockwork gears, Victorian elegance"
        else:
            components["effects"] = ""
        
        return components





