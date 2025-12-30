"""Wildlife photography theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class WildlifePhotoHandler(BaseThemeHandler):
    """Handler for wildlife photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate wildlife photography prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("wildlife_photo.subjects", "wild animal")
        
        composition = self._get_random_choice("wildlife_photo.composition_types", "natural behavior shot")
        
        components["subject"] = (
            f"((wildlife photography)) {subject}, "
            f"{composition}, in natural habitat"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("wildlife_photo.locations", "wilderness")
            lighting = self._get_random_choice("wildlife_photo.lighting", "golden hour light")
            components["environment"] = f"in {location}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("wildlife_photo.styles", "National Geographic style")
            components["style"] = f"{style}, telephoto shot, patient observation"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "natural beauty, wild and free, nature documentary"
        else:
            components["effects"] = ""
        
        return components
