"""Golden hour photography theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class GoldenHourHandler(BaseThemeHandler):
    """Handler for golden hour photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate golden hour photography prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("golden_hour.subjects", "portrait in sunlight")
        
        composition = self._get_random_choice("golden_hour.composition_types", "backlit golden glow")
        
        components["subject"] = (
            f"((golden hour photography)) {subject}, "
            f"{composition}, warm sunset light"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("golden_hour.locations", "open field")
            components["environment"] = f"in {location}, magical hour lighting"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("golden_hour.styles", "natural light portrait")
            components["style"] = f"{style}, warm tones, sun flare"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "golden light, warm glow, lens flare, magical atmosphere"
        else:
            components["effects"] = ""
        
        return components
