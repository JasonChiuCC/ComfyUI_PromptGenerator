"""Demonic theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class DemonicHandler(BaseThemeHandler):
    """Handler for demonic possession horror aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate demonic prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("demonic.demons", "possession demon")
        
        shot_type = self._get_random_choice("demonic.shot_types", "possessed victim contortion")
        possessed_state = self._get_random_choice("demonic.possessed_states", "contorted body")
        element = self._get_random_choice("demonic.elements", "crucifix and rosary")
        mood = self._get_random_choice("demonic.moods", "religious terror")
        
        components["subject"] = (
            f"((demonic horror)) {subject}, "
            f"{shot_type}, {possessed_state}, "
            f"with {element}, {mood}"
        )
        
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                environment = self._get_random_choice("demonic.environments", "bedroom of possessed")
            lighting = self._get_random_choice("demonic.lighting", "candle flicker chaos")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                "demonic horror style, The Exorcist inspired, "
                "possession horror aesthetic, religious terror"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("demonic.effects", "practical contortion")
            components["effects"] = f"{effect}, unholy atmosphere, battle between good and evil"
        else:
            components["effects"] = ""
        
        return components

