"""Hard Sci-Fi theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class HardSciFiHandler(BaseThemeHandler):
    """Handler for hard sci-fi aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate hard sci-fi prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("hard_scifi.subjects", "astronaut in realistic suit")
        
        composition = self._get_random_choice("hard_scifi.composition_types", "documentary style")
        
        components["subject"] = (
            f"((hard sci-fi art)) of {subject}, "
            f"{composition}, scientifically accurate"
        )
        
        if include_environment:
            environment = self._get_random_choice("hard_scifi.environments", "realistic spacecraft interior")
            lighting = self._get_random_choice("hard_scifi.lighting", "realistic space lighting")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("hard_scifi.styles", "NASA aesthetic")
            components["style"] = f"{style}, The Expanse style, realistic physics"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("hard_scifi.effects", "zero gravity")
            components["effects"] = f"{effect}, accurate starfield, scientific realism"
        else:
            components["effects"] = ""
        
        return components





