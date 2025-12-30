"""Couple Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class CoupleHandler(BaseThemeHandler):
    """Handler for Couple portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate couple portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("couple.subjects", "romantic couple")
        
        expression = self._get_random_choice("couple.expressions", "shared loving gaze")
        pose = self._get_random_choice("couple.poses", "intimate embrace")
        outfit = self._get_random_choice("couple.outfits", "coordinated elegant")
        shot_type = self._get_random_choice("couple.shot_types", "romantic portrait")
        
        components["subject"] = (
            f"((couple photography)) of {subject}, "
            f"{expression}, {pose}, wearing {outfit}, {shot_type}"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("couple.locations", "romantic park")
            lighting = self._get_random_choice("couple.lighting", "golden hour warmth")
            components["environment"] = f"in {location}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("couple.styles", "couple photography")
            components["style"] = f"{style}, romantic, connection, love story"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "genuine emotion, intimate connection, timeless romance"
        else:
            components["effects"] = ""
        
        return components
