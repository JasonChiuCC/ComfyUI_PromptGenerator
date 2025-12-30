"""Biopunk theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class BiopunkHandler(BaseThemeHandler):
    """Handler for biopunk aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate biopunk prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("biopunk.subjects", "gene-spliced human")
        
        composition = self._get_random_choice("biopunk.composition_types", "mutation portrait")
        
        components["subject"] = (
            f"((biopunk art)) of {subject}, "
            f"{composition}, organic technology aesthetic"
        )
        
        if include_environment:
            environment = self._get_random_choice("biopunk.environments", "bio-lab facility")
            lighting = self._get_random_choice("biopunk.lighting", "bioluminescent glow")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("biopunk.styles", "biopunk")
            components["style"] = f"{style}, organic mutation, bio-mechanical"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("biopunk.effects", "organic pulsing")
            components["effects"] = f"{effect}, genetic mutation, living tissue"
        else:
            components["effects"] = ""
        
        return components






