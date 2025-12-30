"""Marine Life theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class MarineLifeHandler(BaseThemeHandler):
    """Handler for marine life photography and art."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate marine life prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("marine_life.subjects", "beautiful sea creature")
        
        pose = self._get_random_choice("marine_life.poses", "swimming gracefully")
        expression = self._get_random_choice("marine_life.expressions", "majestic presence")
        shot_type = self._get_random_choice("marine_life.shot_types", "wide ocean scene")
        
        components["subject"] = (
            f"((underwater photography)) of {subject}, "
            f"{pose}, {expression}, {shot_type}"
        )
        
        if include_environment:
            environment = self._get_random_choice("marine_life.environments", "coral reef")
            lighting = self._get_random_choice("marine_life.lighting", "sunbeams through water")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("marine_life.styles", "underwater photography")
            components["style"] = f"{style}, ocean beauty, crystal clear water"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "aquatic wonder, marine majesty, underwater world"
        else:
            components["effects"] = ""
        
        return components






