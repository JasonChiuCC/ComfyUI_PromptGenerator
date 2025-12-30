"""Beauty Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class BeautyHandler(BaseThemeHandler):
    """Handler for Beauty portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate beauty portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("beauty.subjects", "beauty model")
        
        expression = self._get_random_choice("beauty.expressions", "serene beauty")
        pose = self._get_random_choice("beauty.poses", "face tilted slightly")
        makeup = self._get_random_choice("beauty.makeup_styles", "natural glam")
        shot_type = self._get_random_choice("beauty.shot_types", "beauty close-up")
        
        components["subject"] = (
            f"((beauty photography)) of {subject}, "
            f"{expression}, {pose}, {makeup}, {shot_type}"
        )
        
        if include_environment:
            background = self._get_random_choice("beauty.backgrounds", "clean white")
            lighting = self._get_random_choice("beauty.lighting", "beauty dish lighting")
            components["environment"] = f"{background} background, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("beauty.styles", "beauty photography")
            components["style"] = f"{style}, flawless skin, cosmetic quality"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "perfect makeup, radiant, luxury beauty"
        else:
            components["effects"] = ""
        
        return components
