"""Celtic Fantasy theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class CelticFantasyHandler(BaseThemeHandler):
    """Handler for Celtic fantasy aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Celtic fantasy prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("celtic_fantasy.subjects", "druid priest")
        
        shot_type = self._get_random_choice("celtic_fantasy.shot_types", "mystical portrait")
        
        components["subject"] = (
            f"((Celtic fantasy art)) of {subject}, "
            f"{shot_type}, Irish myths and legends"
        )
        
        if include_environment:
            environment = self._get_random_choice("celtic_fantasy.environments", "ancient stone circle")
            lighting = self._get_random_choice("celtic_fantasy.lighting", "misty ethereal")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("celtic_fantasy.styles", "Celtic fantasy")
            components["style"] = f"{style}, Irish mythology, druidic mysticism"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("celtic_fantasy.effects", "Celtic knotwork")
            components["effects"] = f"{effect}, mist and fog, nature magic"
        else:
            components["effects"] = ""
        
        return components





