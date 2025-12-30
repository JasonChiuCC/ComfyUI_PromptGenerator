"""Sports photography theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class SportsPhotoHandler(BaseThemeHandler):
    """Handler for sports photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate sports photography prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("sports_photo.subjects", "athlete in action")
        
        composition = self._get_random_choice("sports_photo.composition_types", "peak action moment")
        
        components["subject"] = (
            f"((sports photography)) {subject}, "
            f"{composition}, frozen motion"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("sports_photo.locations", "stadium")
            components["environment"] = f"at {location}, intense competition"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("sports_photo.styles", "action photography")
            components["style"] = f"{style}, fast shutter speed, telephoto lens"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "frozen action, sharp focus, dynamic energy, peak moment"
        else:
            components["effects"] = ""
        
        return components
