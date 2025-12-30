"""Isekai theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class IsekaiHandler(BaseThemeHandler):
    """Handler for isekai aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate isekai prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("isekai.subjects", "isekai protagonist")
        
        shot_type = self._get_random_choice("isekai.shot_types", "hero pose")
        
        components["subject"] = (
            f"((isekai anime art)) of {subject}, "
            f"{shot_type}, transported to fantasy world"
        )
        
        if include_environment:
            environment = self._get_random_choice("isekai.environments", "fantasy kingdom entrance")
            lighting = self._get_random_choice("isekai.lighting", "anime bright")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("isekai.styles", "isekai anime")
            components["style"] = f"{style}, light novel style, game world aesthetic"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("isekai.effects", "status window UI")
            components["effects"] = f"{effect}, level up glow, power awakening"
        else:
            components["effects"] = ""
        
        return components






