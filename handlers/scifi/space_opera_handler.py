"""Space Opera theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class SpaceOperaHandler(BaseThemeHandler):
    """Handler for space opera aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate space opera prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("space_opera.subjects", "space captain")
        
        composition = self._get_random_choice("space_opera.composition_types", "epic scene")
        
        components["subject"] = (
            f"((space opera art)) of {subject}, "
            f"{composition}, galactic adventure aesthetic"
        )
        
        if include_environment:
            environment = self._get_random_choice("space_opera.environments", "starship bridge")
            lighting = self._get_random_choice("space_opera.lighting", "starlight")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("space_opera.styles", "Star Wars inspired")
            components["style"] = f"{style}, epic sci-fi adventure, cinematic"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("space_opera.effects", "hyperspace streaks")
            components["effects"] = f"{effect}, laser blasts, cosmic grandeur"
        else:
            components["effects"] = ""
        
        return components





