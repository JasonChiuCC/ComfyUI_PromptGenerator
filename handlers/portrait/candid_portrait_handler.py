"""Candid Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class CandidPortraitHandler(BaseThemeHandler):
    """Handler for Candid Portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate candid portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("candid_portrait.subjects", "person")
        
        expression = self._get_random_choice("candid_portrait.expressions", "unguarded moment")
        activity = self._get_random_choice("candid_portrait.activities", "natural activity")
        shot_type = self._get_random_choice("candid_portrait.shot_types", "candid capture")
        
        components["subject"] = (
            f"((candid photography)) of {subject}, "
            f"{expression}, {activity}, {shot_type}"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("candid_portrait.locations", "everyday setting")
            lighting = self._get_random_choice("candid_portrait.lighting", "available light")
            components["environment"] = f"in {location}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("candid_portrait.styles", "candid photography")
            components["style"] = f"{style}, unposed, authentic, real moment"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "genuine emotion, documentary style, spontaneous"
        else:
            components["effects"] = ""
        
        return components
