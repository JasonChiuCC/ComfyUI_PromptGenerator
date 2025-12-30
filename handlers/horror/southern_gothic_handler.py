"""Southern Gothic theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class SouthernGothicHandler(BaseThemeHandler):
    """Handler for Southern Gothic horror aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Southern Gothic prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("southern_gothic.characters", "decaying aristocrat")
        
        shot_type = self._get_random_choice("southern_gothic.shot_types", "plantation house establishing")
        theme = self._get_random_choice("southern_gothic.themes", "family secrets")
        element = self._get_random_choice("southern_gothic.elements", "Spanish moss trees")
        mood = self._get_random_choice("southern_gothic.moods", "oppressive heat")
        
        components["subject"] = (
            f"((Southern Gothic)) {subject}, "
            f"{shot_type}, exploring {theme}, "
            f"with {element}, {mood}"
        )
        
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                environment = self._get_random_choice("southern_gothic.environments", "antebellum mansion")
            lighting = self._get_random_choice("southern_gothic.lighting", "humid hazy sunlight")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                "Southern Gothic style, True Detective inspired, "
                "American South atmosphere, Faulkner aesthetic"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("southern_gothic.effects", "humid atmosphere")
            components["effects"] = f"{effect}, decay and history, sins of the past"
        else:
            components["effects"] = ""
        
        return components

