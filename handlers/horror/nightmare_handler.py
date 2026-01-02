"""Nightmare theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class NightmareHandler(BaseThemeHandler):
    """Handler for nightmare horror aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate nightmare prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("nightmare.subjects", "dreamer victim")
        
        shot_type = self._get_random_choice("nightmare.shot_types", "surreal landscape wide")
        nightmare_type = self._get_random_choice("nightmare.nightmare_types", "chase nightmare")
        element = self._get_random_choice("nightmare.elements", "impossible physics")
        mood = self._get_random_choice("nightmare.moods", "dreaming dread")
        
        components["subject"] = (
            f"((nightmare horror)) {subject}, "
            f"{shot_type}, experiencing {nightmare_type}, "
            f"{element}, {mood}"
        )
        
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                environment = self._get_random_choice("nightmare.environments", "childhood home distorted")
            lighting = self._get_random_choice("nightmare.lighting", "dreamy soft glow")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                "nightmare style, A Nightmare on Elm Street inspired, "
                "surreal dream horror, subconscious terror"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("nightmare.effects", "reality warping")
            components["effects"] = f"{effect}, dreamlike distortion, surreal atmosphere"
        else:
            components["effects"] = ""
        
        return components



