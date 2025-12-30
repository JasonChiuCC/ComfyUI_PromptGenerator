"""Mythical Beasts theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class MythicalBeastsHandler(BaseThemeHandler):
    """Handler for mythical creatures art."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate mythical beasts prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("mythical_beasts.subjects", "legendary creature")
        
        pose = self._get_random_choice("mythical_beasts.poses", "standing proud")
        expression = self._get_random_choice("mythical_beasts.expressions", "ancient wisdom")
        shot_type = self._get_random_choice("mythical_beasts.shot_types", "majestic portrait")
        
        components["subject"] = (
            f"((mythological art)) of {subject}, "
            f"{pose}, {expression}, {shot_type}"
        )
        
        if include_environment:
            environment = self._get_random_choice("mythical_beasts.environments", "ancient temple")
            lighting = self._get_random_choice("mythical_beasts.lighting", "mystical glow")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("mythical_beasts.styles", "mythological art")
            components["style"] = f"{style}, legendary power, epic fantasy"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "ancient legend, mythical grandeur, timeless myth"
        else:
            components["effects"] = ""
        
        return components






