"""Epic Fantasy theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class EpicFantasyHandler(BaseThemeHandler):
    """Handler for epic fantasy aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate epic fantasy prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("epic_fantasy.subjects", "legendary hero")
        
        shot_type = self._get_random_choice("epic_fantasy.shot_types", "epic wide shot")
        
        components["subject"] = (
            f"((epic fantasy art)) of {subject}, "
            f"{shot_type}, grand scale adventure"
        )
        
        if include_environment:
            environment = self._get_random_choice("epic_fantasy.environments", "mountain kingdom")
            lighting = self._get_random_choice("epic_fantasy.lighting", "golden epic light")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("epic_fantasy.styles", "epic fantasy")
            components["style"] = f"{style}, highly detailed, masterpiece"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("epic_fantasy.effects", "magical particles")
            components["effects"] = f"{effect}, legendary atmosphere"
        else:
            components["effects"] = ""
        
        return components





