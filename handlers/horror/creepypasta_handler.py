"""Creepypasta theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class CreepypastaHandler(BaseThemeHandler):
    """Handler for creepypasta internet horror aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate creepypasta prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("creepypasta.entities", "Slenderman-like figure")
        
        shot_type = self._get_random_choice("creepypasta.shot_types", "figure at edge of frame")
        format_type = self._get_random_choice("creepypasta.formats", "found footage")
        element = self._get_random_choice("creepypasta.elements", "static and interference")
        mood = self._get_random_choice("creepypasta.moods", "internet age horror")
        
        components["subject"] = (
            f"((creepypasta horror)) {subject}, "
            f"{shot_type}, {format_type} style, "
            f"{element}, {mood}"
        )
        
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                environment = self._get_random_choice("creepypasta.environments", "abandoned building at night")
            lighting = self._get_random_choice("creepypasta.lighting", "camera flash harsh")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                "creepypasta style, analog horror inspired, "
                "internet urban legend, found footage aesthetic"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("creepypasta.effects", "VHS tracking lines")
            components["effects"] = f"{effect}, digital corruption, unsettling presence"
        else:
            components["effects"] = ""
        
        return components

