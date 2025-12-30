"""Wizard theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class WizardHandler(BaseThemeHandler):
    """Handler for wizard aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate wizard prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("wizard.subjects", "grand wizard")
        
        shot_type = self._get_random_choice("wizard.shot_types", "casting pose")
        
        components["subject"] = (
            f"((wizard art)) of {subject}, "
            f"{shot_type}, magical spellcaster"
        )
        
        if include_environment:
            environment = self._get_random_choice("wizard.environments", "wizard tower study")
            lighting = self._get_random_choice("wizard.lighting", "magical glow")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("wizard.styles", "wizard art")
            components["style"] = f"{style}, arcane power, mystical"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("wizard.effects", "spell casting")
            components["effects"] = f"{effect}, magical runes, arcane energy"
        else:
            components["effects"] = ""
        
        return components






