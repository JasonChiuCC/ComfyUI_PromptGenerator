"""Arabian Fantasy theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class ArabianFantasyHandler(BaseThemeHandler):
    """Handler for Arabian fantasy aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Arabian fantasy prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("arabian_fantasy.subjects", "powerful genie")
        
        shot_type = self._get_random_choice("arabian_fantasy.shot_types", "dramatic genie")
        
        components["subject"] = (
            f"((Arabian fantasy art)) of {subject}, "
            f"{shot_type}, One Thousand and One Nights"
        )
        
        if include_environment:
            environment = self._get_random_choice("arabian_fantasy.environments", "grand palace")
            lighting = self._get_random_choice("arabian_fantasy.lighting", "golden desert sun")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("arabian_fantasy.styles", "Arabian Nights")
            components["style"] = f"{style}, 1001 Nights inspired, exotic fantasy"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("arabian_fantasy.effects", "genie smoke")
            components["effects"] = f"{effect}, magical treasures, wish magic"
        else:
            components["effects"] = ""
        
        return components






