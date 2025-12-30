"""High Fantasy theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class HighFantasyHandler(BaseThemeHandler):
    """Handler for high fantasy aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate high fantasy prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("high_fantasy.subjects", "archmage")
        
        shot_type = self._get_random_choice("high_fantasy.shot_types", "elegant portrait")
        
        components["subject"] = (
            f"((high fantasy art)) of {subject}, "
            f"{shot_type}, magical world aesthetic"
        )
        
        if include_environment:
            environment = self._get_random_choice("high_fantasy.environments", "magical academy")
            lighting = self._get_random_choice("high_fantasy.lighting", "magical radiance")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("high_fantasy.styles", "high fantasy")
            components["style"] = f"{style}, ethereal beauty, enchanting"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("high_fantasy.effects", "floating magic orbs")
            components["effects"] = f"{effect}, magical atmosphere"
        else:
            components["effects"] = ""
        
        return components






