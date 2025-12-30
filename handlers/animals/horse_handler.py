"""Horse theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class HorseHandler(BaseThemeHandler):
    """Handler for horse photography and art."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate horse prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("horse.subjects", "majestic horse")
        
        pose = self._get_random_choice("horse.poses", "galloping free")
        expression = self._get_random_choice("horse.expressions", "noble and proud")
        shot_type = self._get_random_choice("horse.shot_types", "majestic portrait")
        
        components["subject"] = (
            f"((majestic horse)) {subject}, "
            f"{pose}, {expression}, {shot_type}"
        )
        
        if include_environment:
            environment = self._get_random_choice("horse.environments", "open prairie")
            lighting = self._get_random_choice("horse.lighting", "golden hour magic")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("horse.styles", "equine photography")
            components["style"] = f"{style}, powerful and graceful, high quality"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "freedom, wild spirit, equestrian beauty"
        else:
            components["effects"] = ""
        
        return components





