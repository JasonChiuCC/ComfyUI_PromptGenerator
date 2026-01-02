"""Lovecraftian theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class LovecraftianHandler(BaseThemeHandler):
    """Handler for Lovecraftian cosmic horror aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Lovecraftian prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("lovecraftian.entities", "Cthulhu-like Great Old One")
        
        shot_type = self._get_random_choice("lovecraftian.shot_types", "cosmic entity dwarfing human")
        cultist = self._get_random_choice("lovecraftian.cultists", "hooded worshipper")
        element = self._get_random_choice("lovecraftian.elements", "countless tentacles")
        mood = self._get_random_choice("lovecraftian.moods", "cosmic insignificance")
        
        components["subject"] = (
            f"((Lovecraftian cosmic horror)) {subject}, "
            f"{shot_type}, with {cultist}, "
            f"{element}, {mood}"
        )
        
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                environment = self._get_random_choice("lovecraftian.environments", "sunken R'lyeh")
            lighting = self._get_random_choice("lovecraftian.lighting", "eldritch bioluminescence")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                "Lovecraftian style, H.P. Lovecraft inspired, "
                "cosmic horror aesthetic, eldritch nightmare"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("lovecraftian.effects", "sanity distortion")
            components["effects"] = f"{effect}, cosmic scale, unfathomable dread"
        else:
            components["effects"] = ""
        
        return components



