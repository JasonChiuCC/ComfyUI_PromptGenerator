"""Pets theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class PetsHandler(BaseThemeHandler):
    """Handler for pet photography."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate pets prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("pets.subjects", "cute pet")
        
        pose = self._get_random_choice("pets.poses", "being held lovingly")
        expression = self._get_random_choice("pets.expressions", "cute and adorable")
        shot_type = self._get_random_choice("pets.shot_types", "adorable close-up")
        
        components["subject"] = (
            f"((adorable pet photography)) of {subject}, "
            f"{pose}, {expression}, {shot_type}"
        )
        
        if include_environment:
            environment = self._get_random_choice("pets.environments", "cozy home setting")
            lighting = self._get_random_choice("pets.lighting", "soft natural light")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("pets.styles", "pet photography")
            components["style"] = f"{style}, cute and heartwarming, high quality"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "adorable, loveable, professional pet portrait"
        else:
            components["effects"] = ""
        
        return components





