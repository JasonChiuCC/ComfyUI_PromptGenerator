"""Futuristic City theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class FuturisticCityHandler(BaseThemeHandler):
    """Handler for futuristic city art."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate futuristic city prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("futuristic_city.subjects", "megacity skyline")
        
        composition = self._get_random_choice("futuristic_city.composition_types", "skyline panorama")
        
        components["subject"] = (
            f"((futuristic city art)) of {subject}, "
            f"{composition}, advanced urban environment"
        )
        
        if include_environment:
            environment = self._get_random_choice("futuristic_city.environments", "towering megacity")
            lighting = self._get_random_choice("futuristic_city.lighting", "holographic glow")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("futuristic_city.styles", "utopian future")
            components["style"] = f"{style}, high-tech metropolis, stunning detail"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("futuristic_city.effects", "flying vehicles")
            components["effects"] = f"{effect}, holographic displays, advanced technology"
        else:
            components["effects"] = ""
        
        return components





