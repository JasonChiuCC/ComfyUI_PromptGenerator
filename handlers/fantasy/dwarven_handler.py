"""Dwarven theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class DwarvenHandler(BaseThemeHandler):
    """Handler for dwarven aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate dwarven prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("dwarven.subjects", "dwarven king")
        
        shot_type = self._get_random_choice("dwarven.shot_types", "proud portrait")
        
        components["subject"] = (
            f"((dwarven fantasy art)) of {subject}, "
            f"{shot_type}, mountain kingdom dwarf"
        )
        
        if include_environment:
            environment = self._get_random_choice("dwarven.environments", "dwarven mountain hall")
            lighting = self._get_random_choice("dwarven.lighting", "forge fire glow")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("dwarven.styles", "dwarven fantasy")
            components["style"] = f"{style}, sturdy craftsmanship, Norse-inspired"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("dwarven.effects", "forge sparks")
            components["effects"] = f"{effect}, runic glow, gem sparkle"
        else:
            components["effects"] = ""
        
        return components






