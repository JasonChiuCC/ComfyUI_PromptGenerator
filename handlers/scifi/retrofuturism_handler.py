"""Retrofuturism theme handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class RetrofuturismHandler(BaseThemeHandler):
    """Handler for retrofuturism aesthetic."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate retrofuturism prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("retrofuturism.subjects", "retro astronaut")
        
        composition = self._get_random_choice("retrofuturism.composition_types", "advertisement style")
        
        components["subject"] = (
            f"((retrofuturism art)) of {subject}, "
            f"{composition}, past vision of future"
        )
        
        if include_environment:
            environment = self._get_random_choice("retrofuturism.environments", "world's fair pavilion")
            lighting = self._get_random_choice("retrofuturism.lighting", "optimistic bright")
            components["environment"] = f"in {environment}, {lighting}"
        else:
            components["environment"] = ""
        
        if include_style:
            style = self._get_random_choice("retrofuturism.styles", "1950s future vision")
            components["style"] = f"{style}, Jetsons aesthetic, vintage optimism"
        else:
            components["style"] = ""
        
        if include_effects:
            effect = self._get_random_choice("retrofuturism.effects", "jet flames")
            components["effects"] = f"{effect}, bubble domes, chrome shine"
        else:
            components["effects"] = ""
        
        return components





