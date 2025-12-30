"""Encaustic style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class EncausticHandler(BaseThemeHandler):
    """Handler for encaustic painting style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate encaustic painting prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("encaustic.subjects", "abstract expression")
        
        composition = self._get_random_choice("encaustic.composition_types", "layered texture")
        technique = self._get_random_choice("encaustic.techniques", "hot wax application")
        material = self._get_random_choice("encaustic.materials", "beeswax medium")
        
        components["subject"] = (
            f"((encaustic painting)), {subject}, "
            f"{composition}, {technique}, using {material}"
        )
        
        if include_environment:
            effect = self._get_random_choice("encaustic.effects", "translucent layers")
            mood = self._get_random_choice("encaustic.moods", "ancient mystery")
            
            components["environment"] = (
                f"{effect}, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"hot wax painting, ancient technique, "
                f"contemporary encaustic, mixed media quality"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"waxy luminosity, sculptural surface, "
                f"embedded layers, tactile richness"
            )
        else:
            components["effects"] = ""
        
        return components






