"""Witch theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class WitchHandler(BaseThemeHandler):
    """Handler for witch horror aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate witch prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("witch.witch_types", "forest hedge witch")
        
        shot_type = self._get_random_choice("witch.shot_types", "cauldron brewing close-up")
        attire = self._get_random_choice("witch.attire", "flowing black robes")
        element = self._get_random_choice("witch.elements", "bubbling cauldron")
        mood = self._get_random_choice("witch.moods", "mysterious power")
        
        components["subject"] = (
            f"((witch horror)) {subject}, "
            f"{shot_type}, {attire}, with {element}, "
            f"{mood} atmosphere"
        )
        
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                environment = self._get_random_choice("witch.environments", "cottage in dark woods")
            lighting = self._get_random_choice("witch.lighting", "cauldron fire glow")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                "witch horror style, The VVitch inspired, "
                "folk horror aesthetic, dark fairy tale"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("witch.effects", "magical energy swirls")
            components["effects"] = f"{effect}, mystical atmosphere, enchanted ambiance"
        else:
            components["effects"] = ""
        
        return components

