"""Dragon theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class DragonHandler(BaseThemeHandler):
    """Handler for dragon fantasy art."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate dragon prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("dragon.subjects", "majestic dragon")
        
        pose = self._get_random_choice("dragon.poses", "flying majestically")
        expression = self._get_random_choice("dragon.expressions", "fierce and powerful")
        shot_type = self._get_random_choice("dragon.shot_types", "majestic full body")
        
        components["subject"] = (
            f"((epic dragon art)) of {subject}, "
            f"{pose}, {expression}, {shot_type}"
        )
        
        if include_environment:
            environment = self._get_random_choice("dragon.environments", "volcanic mountain")
            lighting = self._get_random_choice("dragon.lighting", "fire glow")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("dragon.styles", "fantasy art")
            components["style"] = f"{style}, epic and legendary, highly detailed"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "scales and flames, ancient power, mythical grandeur"
        else:
            components["effects"] = ""
        
        return components






