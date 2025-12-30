"""Dieselpunk theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class DieselpunkHandler(BaseThemeHandler):
    """Handler for dieselpunk aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate dieselpunk prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("dieselpunk.subjects", "dieselpunk pilot")
        
        composition = self._get_random_choice("dieselpunk.composition_types", "action scene")
        
        components["subject"] = (
            f"((dieselpunk art)) of {subject}, "
            f"{composition}, 1940s retro-future aesthetic"
        )
        
        if include_environment:
            environment = self._get_random_choice("dieselpunk.environments", "art deco metropolis")
            lighting = self._get_random_choice("dieselpunk.lighting", "noir shadows")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("dieselpunk.styles", "dieselpunk")
            components["style"] = f"{style}, art deco futurism, industrial noir"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("dieselpunk.effects", "diesel smoke")
            components["effects"] = f"{effect}, propeller blur, wartime aesthetic"
        else:
            components["effects"] = ""
        
        return components






