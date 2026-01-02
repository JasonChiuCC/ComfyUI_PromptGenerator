"""Zombie theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class ZombieHandler(BaseThemeHandler):
    """Handler for zombie horror aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate zombie prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("zombie.zombie_types", "freshly turned zombie")
        
        shot_type = self._get_random_choice("zombie.shot_types", "horde approaching wide shot")
        decay = self._get_random_choice("zombie.decay_levels", "early decay with wounds")
        element = self._get_random_choice("zombie.elements", "rotting flesh")
        mood = self._get_random_choice("zombie.moods", "apocalyptic dread")
        
        components["subject"] = (
            f"((zombie horror)) {subject}, "
            f"{shot_type}, {decay}, {element}, "
            f"{mood}"
        )
        
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                environment = self._get_random_choice("zombie.environments", "abandoned city streets")
            lighting = self._get_random_choice("zombie.lighting", "overcast apocalypse sky")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                "zombie apocalypse style, George Romero inspired, "
                "survival horror aesthetic, The Walking Dead atmosphere"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("zombie.effects", "blood and gore")
            components["effects"] = f"{effect}, apocalyptic atmosphere, decay and destruction"
        else:
            components["effects"] = ""
        
        return components



