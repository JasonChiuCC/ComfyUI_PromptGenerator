"""Fine Art Portrait theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class FineArtPortraitHandler(BaseThemeHandler):
    """Handler for Fine Art Portrait photography style."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate fine art portrait prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("fine_art_portrait.subjects", "artistic subject")
        
        expression = self._get_random_choice("fine_art_portrait.expressions", "contemplative gaze")
        pose = self._get_random_choice("fine_art_portrait.poses", "sculptural pose")
        outfit = self._get_random_choice("fine_art_portrait.outfits", "flowing fabric")
        shot_type = self._get_random_choice("fine_art_portrait.shot_types", "artistic composition")
        
        components["subject"] = (
            f"((fine art photography)) of {subject}, "
            f"{expression}, {pose}, {outfit}, {shot_type}"
        )
        
        if include_environment:
            background = self._get_random_choice("fine_art_portrait.backgrounds", "painterly background")
            lighting = self._get_random_choice("fine_art_portrait.lighting", "chiaroscuro lighting")
            components["environment"] = f"{background}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("fine_art_portrait.styles", "fine art photography")
            mood = self._get_random_choice("fine_art_portrait.moods", "evocative")
            components["style"] = f"{style}, {mood} mood, gallery quality, museum worthy"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "artistic expression, painterly quality, timeless"
        else:
            components["effects"] = ""
        
        return components
