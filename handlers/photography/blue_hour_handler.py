"""Blue hour photography theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class BlueHourHandler(BaseThemeHandler):
    """Handler for blue hour photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate blue hour photography prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("blue_hour.subjects", "cityscape at dusk")
        
        composition = self._get_random_choice("blue_hour.composition_types", "twilight scene")
        
        components["subject"] = (
            f"((blue hour photography)) {subject}, "
            f"{composition}, cool twilight tones"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("blue_hour.locations", "urban skyline")
            components["environment"] = f"in {location}, dusk atmosphere"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("blue_hour.styles", "twilight photography")
            components["style"] = f"{style}, cool blue tones, city lights emerging"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "blue twilight, city lights, serene atmosphere, dusk magic"
        else:
            components["effects"] = ""
        
        return components
