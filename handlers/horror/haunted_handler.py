"""Haunted theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class HauntedHandler(BaseThemeHandler):
    """Handler for haunted house horror aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate haunted prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("haunted.ghosts", "transparent apparition")
        
        shot_type = self._get_random_choice("haunted.shot_types", "empty room with presence")
        haunting = self._get_random_choice("haunted.haunting_types", "residual energy replay")
        element = self._get_random_choice("haunted.elements", "cold spots")
        mood = self._get_random_choice("haunted.moods", "supernatural dread")
        
        components["subject"] = (
            f"((haunted horror)) {subject}, "
            f"{shot_type}, {haunting}, "
            f"{element}, {mood}"
        )
        
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                environment = self._get_random_choice("haunted.environments", "Victorian haunted house")
            lighting = self._get_random_choice("haunted.lighting", "moonlight through curtains")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                "haunted house style, The Conjuring inspired, "
                "ghost story aesthetic, paranormal investigation"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("haunted.effects", "cold breath visible")
            components["effects"] = f"{effect}, supernatural presence, ghostly atmosphere"
        else:
            components["effects"] = ""
        
        return components



