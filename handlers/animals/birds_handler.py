"""Birds theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class BirdsHandler(BaseThemeHandler):
    """Handler for bird photography and art."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate birds prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("birds.subjects", "beautiful bird")
        
        pose = self._get_random_choice("birds.poses", "perched on branch")
        expression = self._get_random_choice("birds.expressions", "majestic and proud")
        shot_type = self._get_random_choice("birds.shot_types", "perched portrait")
        
        components["subject"] = (
            f"((bird photography)) of {subject}, "
            f"{pose}, {expression}, {shot_type}"
        )
        
        if include_environment:
            environment = self._get_random_choice("birds.environments", "forest canopy")
            lighting = self._get_random_choice("birds.lighting", "bright daylight")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("birds.styles", "bird photography")
            components["style"] = f"{style}, detailed feathers, high quality"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "vibrant colors, nature beauty, wildlife photography"
        else:
            components["effects"] = ""
        
        return components






