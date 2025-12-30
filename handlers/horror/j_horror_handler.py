"""J-Horror theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class JHorrorHandler(BaseThemeHandler):
    """Handler for Japanese horror aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate J-Horror prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("j_horror.spirits", "yurei female ghost")
        
        shot_type = self._get_random_choice("j_horror.shot_types", "static wide shot long tension")
        appearance = self._get_random_choice("j_horror.appearances", "long black hair covering face")
        element = self._get_random_choice("j_horror.elements", "CRT television")
        mood = self._get_random_choice("j_horror.moods", "creeping dread")
        
        components["subject"] = (
            f"((J-Horror Japanese horror)) {subject}, "
            f"{shot_type}, {appearance}, near {element}, "
            f"{mood}"
        )
        
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                environment = self._get_random_choice("j_horror.environments", "Japanese apartment")
            lighting = self._get_random_choice("j_horror.lighting", "blue-grey cold light")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                "J-Horror style, Ringu and Ju-On inspired, "
                "Japanese supernatural horror, Sadako aesthetic"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("j_horror.effects", "VHS distortion")
            components["effects"] = f"{effect}, cold blue atmosphere, unsettling stillness"
        else:
            components["effects"] = ""
        
        return components

