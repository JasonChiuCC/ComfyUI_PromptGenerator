"""Kaiju theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class KaijuHandler(BaseThemeHandler):
    """Handler for kaiju monster art."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate kaiju prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("kaiju.subjects", "giant kaiju monster")
        
        pose = self._get_random_choice("kaiju.poses", "emerging from ocean")
        expression = self._get_random_choice("kaiju.expressions", "terrifying power")
        shot_type = self._get_random_choice("kaiju.shot_types", "towering over city")
        
        components["subject"] = (
            f"((kaiju movie art)) of {subject}, "
            f"{pose}, {expression}, {shot_type}"
        )
        
        if include_environment:
            environment = self._get_random_choice("kaiju.environments", "tokyo cityscape")
            lighting = self._get_random_choice("kaiju.lighting", "nuclear glow")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("kaiju.styles", "kaiju movie style")
            effect = self._get_random_choice("kaiju.effects", "building destruction")
            components["style"] = f"{style}, massive scale, {effect}"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "city destruction, epic scale, monster movie"
        else:
            components["effects"] = ""
        
        return components






