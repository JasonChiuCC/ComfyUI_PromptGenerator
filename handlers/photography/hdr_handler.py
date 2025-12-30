"""HDR photography theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class HDRHandler(BaseThemeHandler):
    """Handler for HDR photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate HDR photography prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("hdr.subjects", "dramatic landscape")
        
        composition = self._get_random_choice("hdr.composition_types", "wide dynamic range")
        
        components["subject"] = (
            f"((HDR photography)) {subject}, "
            f"{composition}, extreme detail"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("hdr.locations", "scenic vista")
            components["environment"] = f"in {location}, full tonal range"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("hdr.styles", "artistic HDR")
            components["style"] = f"{style}, tone mapped, enhanced details"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "HDR effect, vivid colors, shadow and highlight detail, dynamic range"
        else:
            components["effects"] = ""
        
        return components
