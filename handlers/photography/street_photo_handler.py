"""Street photography theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class StreetPhotoHandler(BaseThemeHandler):
    """Handler for street photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate street photography prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("street_photo.subjects", "candid street moment")
        
        composition = self._get_random_choice("street_photo.composition_types", "decisive moment")
        
        components["subject"] = (
            f"((street photography)) {subject}, "
            f"{composition}, authentic urban life"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("street_photo.locations", "busy city street")
            lighting = self._get_random_choice("street_photo.lighting", "natural light")
            components["environment"] = f"in {location}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("street_photo.styles", "documentary style")
            components["style"] = f"{style}, Henri Cartier-Bresson inspired, candid realism"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "natural moment, urban atmosphere, authentic street life"
        else:
            components["effects"] = ""
        
        return components
