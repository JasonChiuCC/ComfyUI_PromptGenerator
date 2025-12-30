"""Alien World theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class AlienWorldHandler(BaseThemeHandler):
    """Handler for alien world art."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate alien world prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("alien_world.subjects", "alien landscape")
        
        composition = self._get_random_choice("alien_world.composition_types", "vast landscape")
        
        components["subject"] = (
            f"((alien world art)) of {subject}, "
            f"{composition}, extraterrestrial environment"
        )
        
        if include_environment:
            environment = self._get_random_choice("alien_world.environments", "twin sun desert")
            lighting = self._get_random_choice("alien_world.lighting", "alien sun color")
            components["environment"] = f"on {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("alien_world.styles", "exoplanet concept")
            components["style"] = f"{style}, otherworldly, cosmic wonder"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("alien_world.effects", "alien atmosphere")
            components["effects"] = f"{effect}, exotic environment, alien beauty"
        else:
            components["effects"] = ""
        
        return components





