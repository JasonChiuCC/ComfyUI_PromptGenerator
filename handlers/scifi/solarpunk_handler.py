"""Solarpunk theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class SolarpunkHandler(BaseThemeHandler):
    """Handler for solarpunk aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate solarpunk prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("solarpunk.subjects", "eco-engineer")
        
        composition = self._get_random_choice("solarpunk.composition_types", "city integration")
        
        components["subject"] = (
            f"((solarpunk art)) of {subject}, "
            f"{composition}, sustainable future aesthetic"
        )
        
        if include_environment:
            environment = self._get_random_choice("solarpunk.environments", "vertical garden city")
            lighting = self._get_random_choice("solarpunk.lighting", "warm sunlight")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("solarpunk.styles", "solarpunk")
            components["style"] = f"{style}, green technology, optimistic eco-future"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("solarpunk.effects", "plant growth")
            components["effects"] = f"{effect}, renewable energy, natural harmony"
        else:
            components["effects"] = ""
        
        return components





