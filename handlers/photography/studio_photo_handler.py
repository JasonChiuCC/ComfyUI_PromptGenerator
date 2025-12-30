"""Studio photography theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class StudioPhotoHandler(BaseThemeHandler):
    """Handler for studio photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate studio photography prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("studio_photo.subjects", "professional model")
        
        shot_type = self._get_random_choice("studio_photo.shot_types", "studio portrait")
        
        components["subject"] = (
            f"((professional studio photography)) {subject}, "
            f"{shot_type}, high-end commercial quality"
        )
        
        if include_environment:
            background = self._get_random_choice("studio_photo.backgrounds", "seamless white backdrop")
            lighting = self._get_random_choice("studio_photo.lighting", "three-point lighting")
            components["environment"] = f"in {background}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("studio_photo.styles", "commercial photography")
            components["style"] = f"{style}, professional lighting setup, magazine quality"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "clean sharp focus, perfect exposure, studio flash"
        else:
            components["effects"] = ""
        
        return components
