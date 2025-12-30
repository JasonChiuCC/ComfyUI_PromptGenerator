"""Lifestyle Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class LifestyleHandler(BaseThemeHandler):
    """Handler for Lifestyle portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate lifestyle portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("lifestyle.subjects", "lifestyle model")
        
        expression = self._get_random_choice("lifestyle.expressions", "genuine laugh")
        pose = self._get_random_choice("lifestyle.poses", "relaxed natural pose")
        outfit = self._get_random_choice("lifestyle.outfits", "casual chic")
        shot_type = self._get_random_choice("lifestyle.shot_types", "candid lifestyle")
        
        components["subject"] = (
            f"((lifestyle photography)) of {subject}, "
            f"{expression}, {pose}, wearing {outfit}, {shot_type}"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("lifestyle.locations", "modern cafe")
            lighting = self._get_random_choice("lifestyle.lighting", "natural window light")
            components["environment"] = f"in {location}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("lifestyle.styles", "lifestyle photography")
            components["style"] = f"{style}, authentic, relatable, aspirational"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "candid feel, modern life, approachable"
        else:
            components["effects"] = ""
        
        return components
