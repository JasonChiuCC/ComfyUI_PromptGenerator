"""Grimdark theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class GrimdarkHandler(BaseThemeHandler):
    """Handler for grimdark aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate grimdark prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("grimdark.subjects", "brutal warlord")
        
        shot_type = self._get_random_choice("grimdark.shot_types", "brutal action")
        
        components["subject"] = (
            f"((grimdark art)) of {subject}, "
            f"{shot_type}, extremely dark brutal fantasy"
        )
        
        if include_environment:
            environment = self._get_random_choice("grimdark.environments", "corpse-strewn battlefield")
            lighting = self._get_random_choice("grimdark.lighting", "blood red")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("grimdark.styles", "grimdark")
            components["style"] = f"{style}, Berserk inspired, nihilistic horror"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("grimdark.effects", "blood splatter")
            components["effects"] = f"{effect}, savage violence, hopeless atmosphere"
        else:
            components["effects"] = ""
        
        return components





