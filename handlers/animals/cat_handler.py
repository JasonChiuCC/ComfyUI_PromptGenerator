"""Cat theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class CatHandler(BaseThemeHandler):
    """Handler for cat photography and art."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate cat prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("cat.subjects", "fluffy cat")
        
        pose = self._get_random_choice("cat.poses", "sitting elegantly")
        expression = self._get_random_choice("cat.expressions", "curious wide eyes")
        shot_type = self._get_random_choice("cat.shot_types", "portrait")
        
        components["subject"] = (
            f"((beautiful cat photography)) of {subject}, "
            f"{pose}, {expression}, {shot_type}"
        )
        
        if include_environment:
            environment = self._get_random_choice("cat.environments", "cozy home")
            lighting = self._get_random_choice("cat.lighting", "soft natural light")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("cat.styles", "pet photography")
            components["style"] = f"{style}, adorable, high quality, sharp focus"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "cute, heartwarming, professional pet portrait"
        else:
            components["effects"] = ""
        
        return components





