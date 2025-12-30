"""Body horror theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class BodyHorrorHandler(BaseThemeHandler):
    """Handler for body horror aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate body horror prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("body_horror.subjects", "mutating victim")
        
        shot_type = self._get_random_choice("body_horror.shot_types", "transformation close-up")
        transformation = self._get_random_choice("body_horror.transformations", "flesh melting and reforming")
        element = self._get_random_choice("body_horror.elements", "exposed muscle and bone")
        mood = self._get_random_choice("body_horror.moods", "visceral disgust")
        
        components["subject"] = (
            f"((body horror)) {subject}, "
            f"{shot_type}, {transformation}, "
            f"{element}, {mood}"
        )
        
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                environment = self._get_random_choice("body_horror.environments", "sterile laboratory")
            lighting = self._get_random_choice("body_horror.lighting", "clinical white light")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                "body horror style, Cronenberg inspired, "
                "The Thing practical effects, grotesque transformation"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("body_horror.effects", "practical prosthetic texture")
            components["effects"] = f"{effect}, visceral detail, biological nightmare"
        else:
            components["effects"] = ""
        
        return components

