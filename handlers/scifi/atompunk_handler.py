"""Atompunk theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class AtompunkHandler(BaseThemeHandler):
    """Handler for atompunk aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate atompunk prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("atompunk.subjects", "atomic age scientist")
        
        composition = self._get_random_choice("atompunk.composition_types", "optimistic future")
        
        components["subject"] = (
            f"((atompunk art)) of {subject}, "
            f"{composition}, 1950s atomic age aesthetic"
        )
        
        if include_environment:
            environment = self._get_random_choice("atompunk.environments", "chrome city")
            lighting = self._get_random_choice("atompunk.lighting", "bright optimistic")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("atompunk.styles", "atompunk")
            components["style"] = f"{style}, googie architecture, space age optimism"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("atompunk.effects", "chrome shine")
            components["effects"] = f"{effect}, ray gun beams, flying cars"
        else:
            components["effects"] = ""
        
        return components






