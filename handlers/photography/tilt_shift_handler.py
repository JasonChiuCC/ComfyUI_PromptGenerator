"""Tilt-shift photography theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class TiltShiftHandler(BaseThemeHandler):
    """Handler for tilt-shift photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate tilt-shift photography prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("tilt_shift.subjects", "miniature city")
        
        composition = self._get_random_choice("tilt_shift.composition_types", "toy-like perspective")
        
        components["subject"] = (
            f"((tilt-shift photography)) {subject}, "
            f"{composition}, miniature model effect"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("tilt_shift.locations", "urban cityscape")
            components["environment"] = f"in {location}, diorama appearance"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("tilt_shift.styles", "miniature effect")
            components["style"] = f"{style}, selective focus, toy town aesthetic"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "miniature effect, selective blur, saturated colors, toy-like"
        else:
            components["effects"] = ""
        
        return components
