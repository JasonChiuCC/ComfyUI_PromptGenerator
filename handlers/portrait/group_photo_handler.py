"""Group Photo theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class GroupPhotoHandler(BaseThemeHandler):
    """Handler for Group Photo photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate group photo prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("group_photo.subjects", "group of friends")
        
        expression = self._get_random_choice("group_photo.expressions", "genuine group laughter")
        pose = self._get_random_choice("group_photo.poses", "casual group arrangement")
        outfit = self._get_random_choice("group_photo.outfits", "coordinated casual")
        shot_type = self._get_random_choice("group_photo.shot_types", "full group wide shot")
        
        components["subject"] = (
            f"((group photography)) of {subject}, "
            f"{expression}, {pose}, wearing {outfit}, {shot_type}"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("group_photo.locations", "outdoor gathering space")
            lighting = self._get_random_choice("group_photo.lighting", "even natural light")
            components["environment"] = f"in {location}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("group_photo.styles", "group photography")
            components["style"] = f"{style}, everyone visible, balanced composition"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "group connection, shared moment, memorable gathering"
        else:
            components["effects"] = ""
        
        return components
