"""Ethereal Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class EtherealHandler(BaseThemeHandler):
    """Handler for Ethereal portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate ethereal portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("ethereal.subjects", "angelic figure")
        
        expression = self._get_random_choice("ethereal.expressions", "dreamy gaze")
        pose = self._get_random_choice("ethereal.poses", "floating gesture")
        outfit = self._get_random_choice("ethereal.outfits", "flowing white dress")
        shot_type = self._get_random_choice("ethereal.shot_types", "soft focus portrait")
        
        components["subject"] = (
            f"((ethereal portrait)) of {subject}, "
            f"{expression}, {pose}, wearing {outfit}, {shot_type}"
        )
        
        if include_environment:
            background = self._get_random_choice("ethereal.backgrounds", "soft bokeh nature")
            lighting = self._get_random_choice("ethereal.lighting", "soft backlighting")
            components["environment"] = f"{background}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("ethereal.styles", "ethereal photography")
            components["style"] = f"{style}, dreamlike, otherworldly, soft romantic"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("ethereal.effects", "soft glow")
            components["effects"] = f"{effect}, angelic, fairytale aesthetic"
        else:
            components["effects"] = ""
        
        return components
