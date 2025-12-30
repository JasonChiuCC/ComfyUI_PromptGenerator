"""Headshot Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class HeadshotHandler(BaseThemeHandler):
    """Handler for Headshot portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate headshot portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("headshot.subjects", "professional person")
        
        expression = self._get_random_choice("headshot.expressions", "warm natural smile")
        pose = self._get_random_choice("headshot.poses", "slight head tilt")
        outfit = self._get_random_choice("headshot.outfits", "professional attire")
        shot_type = self._get_random_choice("headshot.shot_types", "headshot portrait")
        
        components["subject"] = (
            f"((professional headshot)) of {subject}, "
            f"{expression}, {pose}, wearing {outfit}, {shot_type}"
        )
        
        if include_environment:
            background = self._get_random_choice("headshot.backgrounds", "seamless grey")
            lighting = self._get_random_choice("headshot.lighting", "professional headshot lighting")
            components["environment"] = f"{background} background, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("headshot.styles", "headshot photography")
            components["style"] = f"{style}, LinkedIn ready, professional, crisp"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "eyes sharp, professional presence, approachable"
        else:
            components["effects"] = ""
        
        return components
