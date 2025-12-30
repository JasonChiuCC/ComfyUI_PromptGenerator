"""Dramatic Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class DramaticPortraitHandler(BaseThemeHandler):
    """Handler for Dramatic Portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate dramatic portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("dramatic_portrait.subjects", "powerful figure")
        
        expression = self._get_random_choice("dramatic_portrait.expressions", "fierce determination")
        pose = self._get_random_choice("dramatic_portrait.poses", "power pose")
        outfit = self._get_random_choice("dramatic_portrait.outfits", "bold fashion")
        shot_type = self._get_random_choice("dramatic_portrait.shot_types", "hero shot")
        
        components["subject"] = (
            f"((dramatic portrait)) of {subject}, "
            f"{expression}, {pose}, {outfit}, {shot_type}"
        )
        
        if include_environment:
            background = self._get_random_choice("dramatic_portrait.backgrounds", "pure black void")
            lighting = self._get_random_choice("dramatic_portrait.lighting", "hard dramatic light")
            components["environment"] = f"{background}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("dramatic_portrait.styles", "dramatic portrait")
            components["style"] = f"{style}, high-impact, bold, theatrical"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "powerful presence, intense emotion, cinematic drama"
        else:
            components["effects"] = ""
        
        return components
