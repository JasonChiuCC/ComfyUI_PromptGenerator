"""Robot theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class RobotHandler(BaseThemeHandler):
    """Handler for robot and android art."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate robot prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("robot.subjects", "humanoid android")
        
        composition = self._get_random_choice("robot.composition_types", "character portrait")
        
        components["subject"] = (
            f"((robot art)) of {subject}, "
            f"{composition}, mechanical being design"
        )
        
        if include_environment:
            environment = self._get_random_choice("robot.environments", "robot factory")
            lighting = self._get_random_choice("robot.lighting", "LED indicator glow")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("robot.styles", "robot design")
            components["style"] = f"{style}, mechanical aesthetic, detailed"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("robot.effects", "mechanical joints")
            components["effects"] = f"{effect}, chrome surfaces, synthetic life"
        else:
            components["effects"] = ""
        
        return components





