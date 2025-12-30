"""Fairy Tale theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class FairyTaleHandler(BaseThemeHandler):
    """Handler for fairy tale aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate fairy tale prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("fairy_tale.subjects", "beautiful princess")
        
        shot_type = self._get_random_choice("fairy_tale.shot_types", "romantic portrait")
        
        components["subject"] = (
            f"((fairy tale art)) of {subject}, "
            f"{shot_type}, classic storybook fantasy"
        )
        
        if include_environment:
            environment = self._get_random_choice("fairy_tale.environments", "enchanted castle")
            lighting = self._get_random_choice("fairy_tale.lighting", "storybook golden")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("fairy_tale.styles", "fairy tale illustration")
            components["style"] = f"{style}, magical storybook, enchanting"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("fairy_tale.effects", "sparkle dust")
            components["effects"] = f"{effect}, magical transformation"
        else:
            components["effects"] = ""
        
        return components






