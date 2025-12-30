"""Arthurian theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class ArthurianHandler(BaseThemeHandler):
    """Handler for Arthurian legend aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate Arthurian prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("arthurian.subjects", "King Arthur")
        
        shot_type = self._get_random_choice("arthurian.shot_types", "noble portrait")
        
        components["subject"] = (
            f"((Arthurian legend art)) of {subject}, "
            f"{shot_type}, Camelot knights and magic"
        )
        
        if include_environment:
            environment = self._get_random_choice("arthurian.environments", "Camelot castle")
            lighting = self._get_random_choice("arthurian.lighting", "noble golden")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("arthurian.styles", "Arthurian legend")
            components["style"] = f"{style}, medieval romance, chivalric tale"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("arthurian.effects", "Excalibur glow")
            components["effects"] = f"{effect}, magical enchantment, legendary aura"
        else:
            components["effects"] = ""
        
        return components






