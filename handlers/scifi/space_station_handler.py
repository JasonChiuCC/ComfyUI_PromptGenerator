"""Space Station theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class SpaceStationHandler(BaseThemeHandler):
    """Handler for space station art."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate space station prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("space_station.subjects", "rotating space station")
        
        composition = self._get_random_choice("space_station.composition_types", "exterior overview")
        
        components["subject"] = (
            f"((space station art)) of {subject}, "
            f"{composition}, orbital habitat design"
        )
        
        if include_environment:
            environment = self._get_random_choice("space_station.environments", "Earth orbit")
            lighting = self._get_random_choice("space_station.lighting", "Earth light")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("space_station.styles", "realistic sci-fi")
            components["style"] = f"{style}, orbital architecture, detailed"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("space_station.effects", "rotation motion")
            components["effects"] = f"{effect}, docking ships, space habitat"
        else:
            components["effects"] = ""
        
        return components






