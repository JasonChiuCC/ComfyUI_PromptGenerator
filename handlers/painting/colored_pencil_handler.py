"""Colored Pencil style handler."""

from typing import Dict
from ...base_handler import BaseThemeHandler


class ColoredPencilHandler(BaseThemeHandler):
    """Handler for colored pencil style prompt generation."""
    
    def generate(
        self,
        custom_subject: str = "",
        custom_location: str = "",
        include_environment: bool = True,
        include_style: bool = True,
        include_effects: bool = True
    ) -> Dict[str, str]:
        """Generate colored pencil prompt components."""
        components = {}
        
        if custom_subject:
            subject = custom_subject
        else:
            subject = self._get_random_choice("colored_pencil.subjects", "detailed portrait")
        
        composition = self._get_random_choice("colored_pencil.composition_types", "realistic portrait")
        technique = self._get_random_choice("colored_pencil.techniques", "layered building")
        pencil_type = self._get_random_choice("colored_pencil.pencil_types", "artist grade")
        
        components["subject"] = (
            f"((colored pencil art)), {subject}, "
            f"{composition}, {technique}, {pencil_type} pencils"
        )
        
        if include_environment:
            effect = self._get_random_choice("colored_pencil.effects", "smooth gradation")
            mood = self._get_random_choice("colored_pencil.moods", "precise beauty")
            
            components["environment"] = (
                f"{effect}, {mood}"
            )
        else:
            components["environment"] = ""
        
        if include_style:
            components["style"] = (
                f"traditional colored pencil, prismacolor style, "
                f"professional illustration, fine art quality"
            )
        else:
            components["style"] = ""
        
        if include_effects:
            components["effects"] = (
                f"vibrant pigment, waxy finish, "
                f"detailed layers, photorealistic quality"
            )
        else:
            components["effects"] = ""
        
        return components





