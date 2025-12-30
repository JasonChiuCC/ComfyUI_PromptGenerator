"""Dog theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class DogHandler(BaseThemeHandler):
    """Handler for dog photography and art."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate dog prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("dog.subjects", "happy dog")
        
        pose = self._get_random_choice("dog.poses", "sitting obediently")
        expression = self._get_random_choice("dog.expressions", "happy tongue out")
        shot_type = self._get_random_choice("dog.shot_types", "portrait")
        
        components["subject"] = (
            f"((beautiful dog photography)) of {subject}, "
            f"{pose}, {expression}, {shot_type}"
        )
        
        if include_environment:
            environment = self._get_random_choice("dog.environments", "grassy park")
            lighting = self._get_random_choice("dog.lighting", "bright sunny day")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("dog.styles", "pet photography")
            components["style"] = f"{style}, loyal companion, high quality, sharp focus"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "adorable, heartwarming, best friend portrait"
        else:
            components["effects"] = ""
        
        return components





