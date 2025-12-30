"""Sword and Sorcery theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class SwordSorceryHandler(BaseThemeHandler):
    """Handler for sword and sorcery aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate sword and sorcery prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("sword_sorcery.subjects", "barbarian warrior")
        
        shot_type = self._get_random_choice("sword_sorcery.shot_types", "action pose")
        
        components["subject"] = (
            f"((sword and sorcery art)) of {subject}, "
            f"{shot_type}, action-focused fantasy adventure"
        )
        
        if include_environment:
            environment = self._get_random_choice("sword_sorcery.environments", "ancient ruins")
            lighting = self._get_random_choice("sword_sorcery.lighting", "dramatic action")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("sword_sorcery.styles", "sword and sorcery")
            components["style"] = f"{style}, Conan inspired, pulp fantasy"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("sword_sorcery.effects", "magical sword glow")
            components["effects"] = f"{effect}, battle fury, primal power"
        else:
            components["effects"] = ""
        
        return components






