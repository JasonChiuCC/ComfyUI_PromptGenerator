"""Wolf theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class WolfHandler(BaseThemeHandler):
    """Handler for wolf artwork and photography."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate wolf prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("wolf.subjects", "grey wolf")
        
        pose = self._get_random_choice("wolf.poses", "standing majestically")
        expression = self._get_random_choice("wolf.expressions", "fierce intense gaze")
        shot_type = self._get_random_choice("wolf.shot_types", "majestic portrait")
        
        components["subject"] = (
            f"((majestic wolf)) {subject}, "
            f"{pose}, {expression}, {shot_type}"
        )
        
        if include_environment:
            environment = self._get_random_choice("wolf.environments", "snowy mountain")
            lighting = self._get_random_choice("wolf.lighting", "dramatic side light")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("wolf.styles", "wildlife photography")
            components["style"] = f"{style}, wild and powerful, high quality"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "noble, untamed spirit, wilderness majesty"
        else:
            components["effects"] = ""
        
        return components






