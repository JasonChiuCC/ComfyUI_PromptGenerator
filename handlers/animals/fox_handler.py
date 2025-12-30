"""Fox theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class FoxHandler(BaseThemeHandler):
    """Handler for fox artwork and photography."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate fox prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("fox.subjects", "red fox")
        
        pose = self._get_random_choice("fox.poses", "sitting elegantly")
        expression = self._get_random_choice("fox.expressions", "clever cunning look")
        shot_type = self._get_random_choice("fox.shot_types", "portrait close-up")
        
        components["subject"] = (
            f"((beautiful fox)) {subject}, "
            f"{pose}, {expression}, {shot_type}"
        )
        
        if include_environment:
            environment = self._get_random_choice("fox.environments", "autumn forest floor")
            lighting = self._get_random_choice("fox.lighting", "soft golden hour")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("fox.styles", "wildlife photography")
            components["style"] = f"{style}, clever and beautiful, high quality"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "elegant, wild beauty, nature photography"
        else:
            components["effects"] = ""
        
        return components





