"""Occult theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class OccultHandler(BaseThemeHandler):
    """Handler for occult horror aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate occult prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("occult.practitioners", "ceremonial magician")
        
        shot_type = self._get_random_choice("occult.shot_types", "ritual circle wide shot")
        practice = self._get_random_choice("occult.practices", "ritual summoning")
        element = self._get_random_choice("occult.elements", "ancient grimoire")
        mood = self._get_random_choice("occult.moods", "forbidden knowledge")
        
        components["subject"] = (
            f"((occult horror)) {subject}, "
            f"{shot_type}, performing {practice}, "
            f"with {element}, {mood}"
        )
        
        if include_environment:
            if custom_location:
                environment = custom_location
            else:
                environment = self._get_random_choice("occult.environments", "ritual chamber")
            lighting = self._get_random_choice("occult.lighting", "candlelight only")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                "occult horror style, Hereditary inspired, "
                "secret society aesthetic, dark ritual atmosphere"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("occult.effects", "incense smoke swirls")
            components["effects"] = f"{effect}, mystical energy, forbidden ritual"
        else:
            components["effects"] = ""
        
        return components

