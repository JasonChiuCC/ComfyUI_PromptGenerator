"""Post Apocalyptic theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class PostApocalypticHandler(BaseThemeHandler):
    """Handler for post apocalyptic aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate post apocalyptic prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("post_apocalyptic.subjects", "wasteland survivor")
        
        composition = self._get_random_choice("post_apocalyptic.composition_types", "wasteland panorama")
        
        components["subject"] = (
            f"((post apocalyptic art)) of {subject}, "
            f"{composition}, survival aesthetic"
        )
        
        if include_environment:
            environment = self._get_random_choice("post_apocalyptic.environments", "ruined city")
            lighting = self._get_random_choice("post_apocalyptic.lighting", "harsh wasteland sun")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("post_apocalyptic.styles", "Mad Max inspired")
            components["style"] = f"{style}, Fallout aesthetic, survival horror"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("post_apocalyptic.effects", "dust storms")
            components["effects"] = f"{effect}, rust and decay, scavenged gear"
        else:
            components["effects"] = ""
        
        return components






