"""Moody Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class MoodyPortraitHandler(BaseThemeHandler):
    """Handler for Moody Portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate moody portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("moody_portrait.subjects", "mysterious figure")
        
        expression = self._get_random_choice("moody_portrait.expressions", "intense gaze")
        pose = self._get_random_choice("moody_portrait.poses", "shadowed face")
        outfit = self._get_random_choice("moody_portrait.outfits", "dark clothing")
        shot_type = self._get_random_choice("moody_portrait.shot_types", "close-up with shadows")
        
        components["subject"] = (
            f"((moody portrait)) of {subject}, "
            f"{expression}, {pose}, {outfit}, {shot_type}"
        )
        
        if include_environment:
            background = self._get_random_choice("moody_portrait.backgrounds", "deep black")
            lighting = self._get_random_choice("moody_portrait.lighting", "low-key lighting")
            components["environment"] = f"{background}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("moody_portrait.styles", "moody portrait")
            color_tone = self._get_random_choice("moody_portrait.color_tones", "desaturated")
            components["style"] = f"{style}, {color_tone} tones, atmospheric, emotional depth"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "cinematic mood, dramatic shadows, noir-inspired"
        else:
            components["effects"] = ""
        
        return components
