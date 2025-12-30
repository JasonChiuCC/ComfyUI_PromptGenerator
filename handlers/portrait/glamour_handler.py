"""Glamour Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class GlamourHandler(BaseThemeHandler):
    """Handler for Glamour portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate glamour portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("glamour.subjects", "glamorous model")
        
        expression = self._get_random_choice("glamour.expressions", "seductive gaze")
        pose = self._get_random_choice("glamour.poses", "glamour pose")
        outfit = self._get_random_choice("glamour.outfits", "glamorous gown")
        shot_type = self._get_random_choice("glamour.shot_types", "glamour portrait")
        
        components["subject"] = (
            f"((glamour photography)) of {subject}, "
            f"{expression}, {pose}, wearing {outfit}, {shot_type}"
        )
        
        if include_environment:
            background = self._get_random_choice("glamour.backgrounds", "luxury setting")
            lighting = self._get_random_choice("glamour.lighting", "glamour lighting")
            components["environment"] = f"{background}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("glamour.styles", "glamour photography")
            components["style"] = f"{style}, Hollywood glamour, luxurious, sensual"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "red carpet quality, alluring, sophisticated"
        else:
            components["effects"] = ""
        
        return components
