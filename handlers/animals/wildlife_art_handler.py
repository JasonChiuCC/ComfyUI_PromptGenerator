"""Wildlife Art theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class WildlifeArtHandler(BaseThemeHandler):
    """Handler for wildlife art and photography."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate wildlife art prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("wildlife_art.subjects", "majestic lion")
        
        pose = self._get_random_choice("wildlife_art.poses", "in natural habitat")
        expression = self._get_random_choice("wildlife_art.expressions", "powerful and wild")
        shot_type = self._get_random_choice("wildlife_art.shot_types", "portrait close-up")
        
        components["subject"] = (
            f"((wildlife photography)) of {subject}, "
            f"{pose}, {expression}, {shot_type}"
        )
        
        if include_environment:
            environment = self._get_random_choice("wildlife_art.environments", "african savanna")
            lighting = self._get_random_choice("wildlife_art.lighting", "golden african light")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("wildlife_art.styles", "national geographic style")
            components["style"] = f"{style}, nature documentary quality, 8K"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "wild beauty, natural majesty, conservation photography"
        else:
            components["effects"] = ""
        
        return components





