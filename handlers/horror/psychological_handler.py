"""Psychological horror theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class PsychologicalHandler(BaseThemeHandler):
    """Handler for psychological horror aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate psychological horror prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("psychological.subjects", "unreliable narrator")
        
        shot_type = self._get_random_choice("psychological.shot_types", "distorted perspective wide shot")
        mental_state = self._get_random_choice("psychological.mental_states", "paranoid delusion")
        element = self._get_random_choice("psychological.elements", "mirrors everywhere")
        mood = self._get_random_choice("psychological.moods", "creeping paranoia")
        
        components["subject"] = (
            f"((psychological horror)) {subject}, "
            f"{shot_type}, experiencing {mental_state}, "
            f"{element}, {mood}"
        )
        
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                environment = self._get_random_choice("psychological.environments", "empty apartment")
            lighting = self._get_random_choice("psychological.lighting", "harsh interrogation light")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                "psychological horror style, The Shining inspired, "
                "mind-bending thriller, unreliable reality aesthetic"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("psychological.effects", "visual distortion")
            components["effects"] = f"{effect}, unsettling atmosphere, reality questioning"
        else:
            components["effects"] = ""
        
        return components

