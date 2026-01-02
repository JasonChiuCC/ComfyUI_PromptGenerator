"""Slasher theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class SlasherHandler(BaseThemeHandler):
    """Handler for slasher horror aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate slasher prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("slasher.killers", "masked slasher")
        
        shot_type = self._get_random_choice("slasher.shot_types", "killer silhouette in doorway")
        mask = self._get_random_choice("slasher.masks_and_looks", "hockey mask")
        weapon = self._get_random_choice("slasher.weapons", "large kitchen knife")
        mood = self._get_random_choice("slasher.moods", "mounting tension")
        
        components["subject"] = (
            f"((slasher horror)) {subject}, "
            f"{shot_type}, wearing {mask}, holding {weapon}, "
            f"{mood}"
        )
        
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                environment = self._get_random_choice("slasher.environments", "summer camp at night")
            lighting = self._get_random_choice("slasher.lighting", "flickering lights")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                "slasher film style, 1980s horror aesthetic, "
                "Friday the 13th inspired, Halloween atmosphere"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("slasher.effects", "shadow play")
            components["effects"] = f"{effect}, tension building, retro horror film grain"
        else:
            components["effects"] = ""
        
        return components



