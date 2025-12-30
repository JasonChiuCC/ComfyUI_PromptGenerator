"""Dark Fantasy theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class DarkFantasyHandler(BaseThemeHandler):
    """Handler for dark fantasy aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate dark fantasy prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("dark_fantasy.subjects", "dark knight")
        
        shot_type = self._get_random_choice("dark_fantasy.shot_types", "dramatic portrait")
        
        components["subject"] = (
            f"((dark fantasy art)) of {subject}, "
            f"{shot_type}, gothic dark atmosphere"
        )
        
        if include_environment:
            environment = self._get_random_choice("dark_fantasy.environments", "cursed castle")
            lighting = self._get_random_choice("dark_fantasy.lighting", "blood moon glow")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("dark_fantasy.styles", "dark fantasy")
            components["style"] = f"{style}, Dark Souls inspired, ominous"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("dark_fantasy.effects", "dark magic swirls")
            components["effects"] = f"{effect}, cursed atmosphere"
        else:
            components["effects"] = ""
        
        return components






