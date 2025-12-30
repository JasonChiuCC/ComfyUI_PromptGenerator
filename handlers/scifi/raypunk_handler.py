"""Raypunk theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class RaypunkHandler(BaseThemeHandler):
    """Handler for raypunk aesthetic - pre-1950s retro sci-fi."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate raypunk prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("raypunk.subjects", "ray gun hero")
        
        composition = self._get_random_choice("raypunk.composition_types", "movie serial poster")
        
        components["subject"] = (
            f"((raypunk art)) of {subject}, "
            f"{composition}, 1930s sci-fi serial aesthetic"
        )
        
        if include_environment:
            environment = self._get_random_choice("raypunk.environments", "cardboard spaceship")
            lighting = self._get_random_choice("raypunk.lighting", "theatrical spotlight")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("raypunk.styles", "Flash Gordon aesthetic")
            components["style"] = f"{style}, handmade prop charm, theatrical"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("raypunk.effects", "ray gun sparks")
            components["effects"] = f"{effect}, visible wires, stage set magic"
        else:
            components["effects"] = ""
        
        return components





