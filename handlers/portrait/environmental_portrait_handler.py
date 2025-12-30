"""Environmental Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class EnvironmentalPortraitHandler(BaseThemeHandler):
    """Handler for Environmental Portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate environmental portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("environmental_portrait.subjects", "person in environment")
        
        expression = self._get_random_choice("environmental_portrait.expressions", "natural candid")
        pose = self._get_random_choice("environmental_portrait.poses", "natural working pose")
        shot_type = self._get_random_choice("environmental_portrait.shot_types", "wide environmental")
        
        components["subject"] = (
            f"((environmental portrait)) of {subject}, "
            f"{expression}, {pose}, {shot_type}"
        )
        
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                environment = self._get_random_choice("environmental_portrait.environments", "meaningful location")
            lighting = self._get_random_choice("environmental_portrait.lighting", "natural ambient")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("environmental_portrait.styles", "environmental portrait")
            components["style"] = f"{style}, contextual storytelling, authentic"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "documentary quality, narrative portrait"
        else:
            components["effects"] = ""
        
        return components
