"""Survival horror theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class SurvivalHorrorHandler(BaseThemeHandler):
    """Handler for survival horror game aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate survival horror prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("survival_horror.protagonists", "unprepared survivor")
        
        shot_type = self._get_random_choice("survival_horror.shot_types", "over-shoulder third person")
        monster = self._get_random_choice("survival_horror.monsters", "zombie variants")
        element = self._get_random_choice("survival_horror.elements", "limited ammunition")
        mood = self._get_random_choice("survival_horror.moods", "resource anxiety")
        
        components["subject"] = (
            f"((survival horror)) {subject}, "
            f"{shot_type}, facing {monster}, "
            f"{element}, {mood}"
        )
        
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                environment = self._get_random_choice("survival_horror.environments", "abandoned mansion")
            lighting = self._get_random_choice("survival_horror.lighting", "flashlight cone")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                "survival horror game style, Resident Evil inspired, "
                "Silent Hill atmosphere, video game horror aesthetic"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("survival_horror.effects", "grain and noise")
            components["effects"] = f"{effect}, limited visibility, tension and dread"
        else:
            components["effects"] = ""
        
        return components



