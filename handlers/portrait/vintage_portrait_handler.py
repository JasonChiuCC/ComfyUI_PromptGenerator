"""Vintage Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class VintagePortraitHandler(BaseThemeHandler):
    """Handler for Vintage Portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate vintage portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("vintage_portrait.subjects", "classic person")
        
        expression = self._get_random_choice("vintage_portrait.expressions", "timeless expression")
        pose = self._get_random_choice("vintage_portrait.poses", "classic pose")
        outfit = self._get_random_choice("vintage_portrait.outfits", "period appropriate attire")
        shot_type = self._get_random_choice("vintage_portrait.shot_types", "classic portrait")
        era = self._get_random_choice("vintage_portrait.eras", "1950s")
        
        components["subject"] = (
            f"(({era} vintage portrait)) of {subject}, "
            f"{expression}, {pose}, wearing {outfit}, {shot_type}"
        )
        
        if include_environment:
            background = self._get_random_choice("vintage_portrait.backgrounds", "classic backdrop")
            lighting = self._get_random_choice("vintage_portrait.lighting", "vintage studio lighting")
            components["environment"] = f"{background}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("vintage_portrait.styles", "vintage photography")
            film_type = self._get_random_choice("vintage_portrait.film_types", "film grain")
            components["style"] = f"{style}, {film_type}, nostalgic, period authentic"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "vintage film look, classic era, timeless elegance"
        else:
            components["effects"] = ""
        
        return components
