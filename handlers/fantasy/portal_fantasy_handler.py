"""Portal Fantasy theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class PortalFantasyHandler(BaseThemeHandler):
    """Handler for portal fantasy aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate portal fantasy prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("portal_fantasy.subjects", "transported hero")
        
        shot_type = self._get_random_choice("portal_fantasy.shot_types", "discovery moment")
        
        components["subject"] = (
            f"((portal fantasy art)) of {subject}, "
            f"{shot_type}, transported to another world"
        )
        
        if include_environment:
            environment = self._get_random_choice("portal_fantasy.environments", "portal gateway")
            lighting = self._get_random_choice("portal_fantasy.lighting", "portal glow")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("portal_fantasy.styles", "portal fantasy")
            components["style"] = f"{style}, dimensional travel, new world wonder"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("portal_fantasy.effects", "portal energy")
            components["effects"] = f"{effect}, reality warping"
        else:
            components["effects"] = ""
        
        return components





