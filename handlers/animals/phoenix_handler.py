"""Phoenix theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class PhoenixHandler(BaseThemeHandler):
    """Handler for phoenix fantasy art."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate phoenix prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("phoenix.subjects", "rising phoenix")
        
        pose = self._get_random_choice("phoenix.poses", "rising from flames")
        expression = self._get_random_choice("phoenix.expressions", "fierce and powerful")
        shot_type = self._get_random_choice("phoenix.shot_types", "dramatic rising")
        
        components["subject"] = (
            f"((epic phoenix art)) of {subject}, "
            f"{pose}, {expression}, {shot_type}"
        )
        
        if include_environment:
            environment = self._get_random_choice("phoenix.environments", "burning inferno")
            lighting = self._get_random_choice("phoenix.lighting", "intense fire glow")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("phoenix.styles", "fantasy art")
            effect = self._get_random_choice("phoenix.effects", "trailing flames")
            components["style"] = f"{style}, legendary firebird, {effect}"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "fire and rebirth, ember particles, immortal glory"
        else:
            components["effects"] = ""
        
        return components






