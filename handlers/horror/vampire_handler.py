"""Vampire theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class VampireHandler(BaseThemeHandler):
    """Handler for vampire horror aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate vampire prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("vampire.characters", "ancient vampire lord")
        
        shot_type = self._get_random_choice("vampire.shot_types", "dramatic portrait in candlelight")
        attire = self._get_random_choice("vampire.attire", "flowing black cape")
        element = self._get_random_choice("vampire.elements", "exposed fangs")
        mood = self._get_random_choice("vampire.moods", "seductive danger")
        
        components["subject"] = (
            f"((vampire horror)) {subject}, "
            f"{shot_type}, {attire}, {element}, "
            f"{mood} atmosphere"
        )
        
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                environment = self._get_random_choice("vampire.environments", "gothic castle interior")
            lighting = self._get_random_choice("vampire.lighting", "candlelight and shadow")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                "gothic horror style, Bram Stoker inspired, "
                "dark romantic aesthetic, cinematic vampire film"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("vampire.effects", "blood mist")
            components["effects"] = f"{effect}, dramatic shadows, crimson accents"
        else:
            components["effects"] = ""
        
        return components



