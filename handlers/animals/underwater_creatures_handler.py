"""Underwater Creatures theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class UnderwaterCreaturesHandler(BaseThemeHandler):
    """Handler for deep sea creatures art."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate underwater creatures prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("underwater_creatures.subjects", "deep sea creature")
        
        pose = self._get_random_choice("underwater_creatures.poses", "floating in darkness")
        expression = self._get_random_choice("underwater_creatures.expressions", "alien and mysterious")
        shot_type = self._get_random_choice("underwater_creatures.shot_types", "creature portrait")
        
        components["subject"] = (
            f"((deep sea photography)) of {subject}, "
            f"{pose}, {expression}, {shot_type}"
        )
        
        if include_environment:
            environment = self._get_random_choice("underwater_creatures.environments", "abyssal depths")
            lighting = self._get_random_choice("underwater_creatures.lighting", "bioluminescence")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("underwater_creatures.styles", "deep sea photography")
            components["style"] = f"{style}, mysterious and eerie, otherworldly"
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = "bioluminescent glow, deep ocean mystery, alien beauty"
        else:
            components["effects"] = ""
        
        return components






