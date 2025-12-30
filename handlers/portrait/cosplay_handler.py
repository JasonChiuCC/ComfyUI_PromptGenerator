"""Cosplay Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class CosplayHandler(BaseThemeHandler):
    """Handler for Cosplay portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate cosplay portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("cosplay.subjects", "cosplayer in costume")
        
        expression = self._get_random_choice("cosplay.expressions", "in-character expression")
        pose = self._get_random_choice("cosplay.poses", "character signature pose")
        costume = self._get_random_choice("cosplay.costumes", "detailed handmade costume")
        shot_type = self._get_random_choice("cosplay.shot_types", "full costume shot")
        
        components["subject"] = (
            f"((cosplay photography)) of {subject}, "
            f"{expression}, {pose}, {costume}, {shot_type}"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("cosplay.locations", "themed backdrop")
            lighting = self._get_random_choice("cosplay.lighting", "cosplay photography lighting")
            components["environment"] = f"in {location}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("cosplay.styles", "cosplay photography")
            components["style"] = f"{style}, accurate character, professional cosplay"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("cosplay.effects", "character energy")
            components["effects"] = f"{effect}, convention quality, character accuracy"
        else:
            components["effects"] = ""
        
        return components
