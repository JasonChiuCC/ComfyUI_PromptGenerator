"""Editorial Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class EditorialHandler(BaseThemeHandler):
    """Handler for Editorial portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate editorial portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("editorial.subjects", "editorial model")
        
        expression = self._get_random_choice("editorial.expressions", "editorial attitude")
        pose = self._get_random_choice("editorial.poses", "editorial pose")
        outfit = self._get_random_choice("editorial.outfits", "designer ensemble")
        shot_type = self._get_random_choice("editorial.shot_types", "editorial composition")
        
        components["subject"] = (
            f"((editorial photography)) of {subject}, "
            f"{expression}, {pose}, wearing {outfit}, {shot_type}"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("editorial.locations", "urban setting")
            lighting = self._get_random_choice("editorial.lighting", "natural editorial light")
            components["environment"] = f"in {location}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("editorial.styles", "editorial photography")
            components["style"] = f"{style}, magazine quality, storytelling"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "publication ready, artistic narrative, contemporary"
        else:
            components["effects"] = ""
        
        return components
