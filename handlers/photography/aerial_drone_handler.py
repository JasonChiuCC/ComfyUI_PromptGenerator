"""Aerial drone photography theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class AerialDroneHandler(BaseThemeHandler):
    """Handler for aerial drone photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate aerial drone photography prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("aerial_drone.subjects", "landscape from above")
        
        composition = self._get_random_choice("aerial_drone.composition_types", "bird's eye view")
        
        components["subject"] = (
            f"((aerial drone photography)) {subject}, "
            f"{composition}, stunning perspective"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("aerial_drone.locations", "scenic landscape")
            components["environment"] = f"aerial view of {location}, high altitude shot"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("aerial_drone.styles", "professional drone footage")
            components["style"] = f"{style}, DJI quality, cinematic aerial"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "bird's eye perspective, vast scale, drone cinematography"
        else:
            components["effects"] = ""
        
        return components
