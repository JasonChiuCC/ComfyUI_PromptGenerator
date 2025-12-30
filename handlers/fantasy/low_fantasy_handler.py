"""Low Fantasy theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class LowFantasyHandler(BaseThemeHandler):
    """Handler for low fantasy aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate low fantasy prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("low_fantasy.subjects", "sellsword mercenary")
        
        shot_type = self._get_random_choice("low_fantasy.shot_types", "gritty portrait")
        
        components["subject"] = (
            f"((low fantasy art)) of {subject}, "
            f"{shot_type}, gritty realistic medieval"
        )
        
        if include_environment:
            environment = self._get_random_choice("low_fantasy.environments", "muddy battlefield")
            lighting = self._get_random_choice("low_fantasy.lighting", "overcast gloomy")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("low_fantasy.styles", "low fantasy")
            components["style"] = f"{style}, Game of Thrones inspired, realistic"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("low_fantasy.effects", "blood and mud")
            components["effects"] = f"{effect}, weathered, battle-worn"
        else:
            components["effects"] = ""
        
        return components






