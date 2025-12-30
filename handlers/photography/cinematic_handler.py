"""Cinematic photography theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class CinematicHandler(BaseThemeHandler):
    """Handler for cinematic photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate cinematic photography prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("cinematic.subjects", "dramatic portrait")
        
        shot_type = self._get_random_choice("cinematic.shot_types", "wide establishing shot")
        
        components["subject"] = (
            f"((cinematic photography)) {subject}, "
            f"{shot_type}, movie still quality"
        )
        
        if include_environment:
            lighting = self._get_random_choice("cinematic.lighting", "dramatic chiaroscuro")
            components["environment"] = f"{lighting}, atmospheric scene"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("cinematic.styles", "cinematic photography")
            color_grade = self._get_random_choice("cinematic.color_grades", "teal and orange")
            components["style"] = f"{style}, {color_grade} color grading, 35mm film, anamorphic"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "cinematic lighting, film grain, high production value"
        else:
            components["effects"] = ""
        
        return components
