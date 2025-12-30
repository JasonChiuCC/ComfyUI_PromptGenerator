"""Colony Planet theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class ColonyPlanetHandler(BaseThemeHandler):
    """Handler for colony planet art."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate colony planet prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("colony_planet.subjects", "pioneer colonist")
        
        composition = self._get_random_choice("colony_planet.composition_types", "colony overview")
        
        components["subject"] = (
            f"((colony planet art)) of {subject}, "
            f"{composition}, space colonization aesthetic"
        )
        
        if include_environment:
            environment = self._get_random_choice("colony_planet.environments", "Mars colony")
            lighting = self._get_random_choice("colony_planet.lighting", "dome-filtered light")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("colony_planet.styles", "colonization sci-fi")
            components["style"] = f"{style}, frontier future, pioneering spirit"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("colony_planet.effects", "atmospheric processors")
            components["effects"] = f"{effect}, terraforming, survival sci-fi"
        else:
            components["effects"] = ""
        
        return components






