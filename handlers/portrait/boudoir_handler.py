"""Boudoir Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class BoudoirHandler(BaseThemeHandler):
    """Handler for Boudoir portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate boudoir portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("boudoir.subjects", "elegant woman")
        
        expression = self._get_random_choice("boudoir.expressions", "confident sensuality")
        pose = self._get_random_choice("boudoir.poses", "elegant boudoir pose")
        outfit = self._get_random_choice("boudoir.outfits", "silk lingerie")
        shot_type = self._get_random_choice("boudoir.shot_types", "tasteful boudoir")
        
        components["subject"] = (
            f"((boudoir photography)) of {subject}, "
            f"{expression}, {pose}, wearing {outfit}, {shot_type}"
        )
        
        if include_environment:
            if custom_location:
                location = custom_location
            else:
                location = self._get_random_choice("boudoir.locations", "luxurious bedroom")
            lighting = self._get_random_choice("boudoir.lighting", "soft natural light")
            components["environment"] = f"in {location}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("boudoir.styles", "boudoir photography")
            components["style"] = f"{style}, intimate, empowering, tasteful"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "romantic atmosphere, soft sensuality, elegant"
        else:
            components["effects"] = ""
        
        return components
